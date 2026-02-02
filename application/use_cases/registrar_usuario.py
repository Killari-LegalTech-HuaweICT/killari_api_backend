#application/use_cases/registrar_usuario.py
from domains.entities.usuario import Usuario
from domains.interfaces.usuario_repository import UsuarioRepository

class RegistrarUsuario:
    def __init__(self, usuario_repo: UsuarioRepository):
        self.usuario_repo = usuario_repo

    def ejecutar(self, dni: str, nombres: str, apellidos: str, password: str, rol: str = "USER"):
        usuario_existente = self.usuario_repo.obtener_por_dni(dni)
        if usuario_existente:
            raise Exception("Usuario ya existe")
        nuevo_usuario = Usuario(dni, nombres, apellidos, password, rol)
        return self.usuario_repo.crear(nuevo_usuario)