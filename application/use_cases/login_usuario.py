#application/use_cases/login_usuario.py
from domains.interfaces.usuario_repository import UsuarioRepository
import jwt
from datetime import datetime, timedelta

# Clave secreta para firmar el JWT
SECRET_KEY = "mi_clave_super_secreta"

class LoginUsuario:
    def __init__(self, usuario_repo: UsuarioRepository):
        self.usuario_repo = usuario_repo

    def ejecutar(self, dni: str, password: str):

        usuario = self.usuario_repo.obtener_por_dni(dni)
        if not usuario:
            raise Exception("Usuario no encontrado")


        if not usuario.verificar_password(password):
            raise Exception("Password incorrecta")

        #Crear el payload del token JWT
        payload = {
            "dni": usuario.dni,
            "nombres": usuario.nombres,
            "rol": usuario.rol,
            "exp": datetime.utcnow() + timedelta(hours=1)  # Expira en 1 hora
        }


        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

        #Devolver el usuario + token
        return {
            "token": token,
            "usuario": {
                "dni": usuario.dni,
                "nombres": usuario.nombres,
                "rol": usuario.rol
            }
        }