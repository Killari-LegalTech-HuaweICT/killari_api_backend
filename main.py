# Punto de entrada de FastAPI. Inyeccion de dependencias. 
# main.py
from flask import Flask
from infrastructure.persistence.usuario_model import db, UsuarioModel
from infrastructure.persistence.agraviado_model import AgraviadoModel
from infrastructure.persistence.caso_model import CasoModel
from infrastructure.persistence.elemento_conviccion_model import ElementoConviccionModel
from infrastructure.api.usuario_controller import auth_bp  # Blueprint de login/register

def create_app():
    app = Flask(__name__)
    
    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sistema_killari.db'  # Nombre más representativo
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicialización de SQLAlchemy
    db.init_app(app)

    # Registro de Blueprints (Endpoints)
    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')

    # Crear todas las tablas si no existen
    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)