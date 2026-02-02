from infrastructure.persistence.usuario_model import db

class ElementoConviccionModel(db.Model):
    __tablename__ = "elemento_conviccion"

    id_elemento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_caso = db.Column(db.Integer, db.ForeignKey("caso.id_caso", ondelete="CASCADE"), nullable=False)
    tipo = db.Column(db.String(20))  # DOCUMENTO, AUDIO, VIDEO, OTRO
    descripcion = db.Column(db.Text)
    archivo_url = db.Column(db.Text)
    audio_url = db.Column(db.Text)
    transcripcion = db.Column(db.Text)
    boceto_redactado = db.Column(db.Text)
    fecha_registro = db.Column(db.DateTime, server_default=db.func.current_timestamp())
