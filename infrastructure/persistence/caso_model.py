#infrastructure/persistence/caso_model.py
from infrastructure.persistence.usuario_model import db

class CasoModel(db.Model):
    __tablename__ = "caso"

    id_caso = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero_caso = db.Column(db.String(50), nullable=False)
    tipo_caso = db.Column(db.String(100))
    fecha_registro = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    estado = db.Column(db.String(20), default="ABIERTO")
    dni_usuario = db.Column(db.String(8), db.ForeignKey("usuario.dni"), nullable=False)
    dni_agraviado = db.Column(db.String(8), db.ForeignKey("agraviado.dni"), nullable=False)
