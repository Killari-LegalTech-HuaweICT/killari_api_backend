#infrastructure/persistence/agraviado_repository_impl.py
from domains.interfaces.agraviado_repository import AgraviadoRepository
from domains.entities.agraviado import Agraviado
from infrastructure.persistence.agraviado_model import AgraviadoModel, db

class AgraviadoRepositoryImpl(AgraviadoRepository):

    def crear(self, agraviado: Agraviado) -> Agraviado:
        modelo = AgraviadoModel(
            dni=agraviado.dni,
            nombres=agraviado.nombres,
            apellidos=agraviado.apellidos,
            fecha_nacimiento=agraviado.fecha_nacimiento,
            direccion=agraviado.direccion,
            telefono=agraviado.telefono
        )
        db.session.add(modelo)
        db.session.commit()
        return agraviado

    def obtener_por_dni(self, dni: str) -> Agraviado:
        a = AgraviadoModel.query.filter_by(dni=dni).first()
        if a:
            return Agraviado(
                dni=a.dni,
                nombres=a.nombres,
                apellidos=a.apellidos,
                fecha_nacimiento=a.fecha_nacimiento,
                direccion=a.direccion,
                telefono=a.telefono
            )
        return None
