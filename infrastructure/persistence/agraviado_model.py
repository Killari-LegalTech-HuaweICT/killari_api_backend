#infrastructure/persistence/agraviado_model.py
from infrastructure.persistence.usuario_model import db

class AgraviadoModel(db.Model):
    __tablename__ = "agraviado"

    dni = db.Column(db.String(8), primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date)
    direccion = db.Column(db.Text)
    telefono = db.Column(db.String(20))
