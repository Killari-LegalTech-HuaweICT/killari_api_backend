#infrastructure/persistence/usuario_model.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UsuarioModel(db.Model):
    __tablename__ = 'usuario'

    dni = db.Column(db.String(8), primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.Enum('ADMIN', 'USER', 'INVITADO'), default='USER')
    estado = db.Column(db.Integer, default=1)