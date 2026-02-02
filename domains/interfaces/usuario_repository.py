#domain/interfaces/usuario_repository.py
from abc import ABC, abstractmethod
from domains.entities.usuario import Usuario

class UsuarioRepository(ABC):

    @abstractmethod
    def crear(self, usuario: Usuario) -> Usuario:
        pass

    @abstractmethod
    def obtener_por_dni(self, dni: str) -> Usuario:
        pass

    @abstractmethod
    def obtener_por_email(self, email: str) -> Usuario:
        pass