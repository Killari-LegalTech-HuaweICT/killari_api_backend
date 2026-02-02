#infrastructure/persistence/usuario_repository_impl.py
from domains.interfaces.usuario_repository import UsuarioRepository
from domains.entities.usuario import Usuario
from infrastructure.persistence.usuario_model import UsuarioModel, db
from werkzeug.security import generate_password_hash

class UsuarioRepositoryImpl(UsuarioRepository):

    def crear(self, usuario: Usuario) -> Usuario:
        hashed_password = generate_password_hash(usuario.password)
        usuario_model = UsuarioModel(
            dni=usuario.dni,
            nombres=usuario.nombres,
            apellidos=usuario.apellidos,
            password=hashed_password,
            rol=usuario.rol,
            estado=usuario.estado
        )
        db.session.add(usuario_model)
        db.session.commit()
        return usuario

    def obtener_por_dni(self, dni: str) -> Usuario:
        u = UsuarioModel.query.filter_by(dni=dni).first()
        if u:
            return Usuario(
                dni=u.dni,
                nombres=u.nombres,
                apellidos=u.apellidos,
                password=u.password,
                rol=u.rol,
                estado=u.estado
            )
        return None

    def obtener_por_email(self, email: str) -> Usuario:
        # Como usamos DNI, por ahora lo dejamos como ejemplo
        return None