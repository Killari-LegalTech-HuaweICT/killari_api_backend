#infrastructure/persistence/caso_repository_impl.py
from domains.interfaces.caso_repository import CasoRepository
from domains.entities.caso import Caso
from infrastructure.persistence.caso_model import CasoModel, db

class CasoRepositoryImpl(CasoRepository):

    def crear(self, caso: Caso) -> Caso:
        modelo = CasoModel(
            numero_caso=caso.numero_caso,
            tipo_caso=caso.tipo_caso,
            estado=caso.estado,
            dni_usuario=caso.dni_usuario,
            dni_agraviado=caso.dni_agraviado
        )
        db.session.add(modelo)
        db.session.commit()
        caso.id_caso = modelo.id_caso
        return caso

    def obtener_por_id(self, id_caso: int) -> Caso:
        c = CasoModel.query.filter_by(id_caso=id_caso).first()
        if c:
            return Caso(
                id_caso=c.id_caso,
                numero_caso=c.numero_caso,
                tipo_caso=c.tipo_caso,
                estado=c.estado,
                dni_usuario=c.dni_usuario,
                dni_agraviado=c.dni_agraviado
            )
        return None
