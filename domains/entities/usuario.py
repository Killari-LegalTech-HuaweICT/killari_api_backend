#domains/entities/usuario.py
class Usuario:
    def __init__(self, dni: str, nombres: str, apellidos: str, password: str, rol: str = "USER", estado: int = 1):
        self.dni = dni
        self.nombres = nombres
        self.apellidos = apellidos
        self.password = password  # aquí guardaremos el hash
        self.rol = rol
        self.estado = estado

    def verificar_password(self, password_plain: str) -> bool:
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password_plain)