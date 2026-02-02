#infrastructure/api/usuario_controller.py
from flask import Blueprint, request, jsonify
from infrastructure.persistence.usuario_repository_impl import UsuarioRepositoryImpl
from application.use_cases.registrar_usuario import RegistrarUsuario
from application.use_cases.login_usuario import LoginUsuario
from infrastructure.api.security import token_required


# Definimos el Blueprint
auth_bp = Blueprint('auth', __name__)

SECRET_KEY = "mi_clave_super_secreta"

# Instanciamos el repositorio (En arquitecturas más pro usarías un inyector, 
# pero esto es correcto para empezar)
usuario_repo = UsuarioRepositoryImpl()


#end para el register

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    caso_uso = RegistrarUsuario(usuario_repo)
    try:
        usuario = caso_uso.ejecutar(
            dni=data["dni"],
            nombres=data["nombres"],
            apellidos=data["apellidos"],
            password=data["password"],
            rol=data.get("rol", "USER")
        )
        return jsonify({"dni": usuario.dni, "nombres": usuario.nombres}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

#end para el login

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    caso_uso = LoginUsuario(usuario_repo)
    try:
        resultado = caso_uso.ejecutar(dni=data["dni"], password=data["password"])
        # 'resultado' ya contiene token y usuario
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
#end para probar el decorador de seguridad

@auth_bp.route("/perfil", methods=["GET"])
@token_required
def perfil():
    usuario = request.user
    return jsonify({
        "mensaje": f"Hola {usuario['nombres']}, tu rol es {usuario['rol']}",
        "dni": usuario["dni"]
    })