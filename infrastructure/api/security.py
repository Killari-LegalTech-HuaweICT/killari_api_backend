#infraestructure/api/security.py
import jwt
from functools import wraps
from flask import request, jsonify

SECRET_KEY = "mi_clave_super_secreta"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"error": "Token faltante"}), 401
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            request.user = payload  # Guardamos info del usuario para usar en la ruta
        except Exception as e:
            return jsonify({"error": "Token inválido"}), 401
        return f(*args, **kwargs)
    return decorated