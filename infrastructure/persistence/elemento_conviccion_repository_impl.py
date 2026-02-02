from domains.interfaces.elemento_conviccion_repository import ElementoConviccionRepository
from domains.entities.elemento_conviccion import ElementoConviccion
from infrastructure.persistence.elemento_conviccion_model import ElementoConviccionModel, db

class ElementoConviccionRepositoryImpl(ElementoConviccionRepository):

    def crear(self, elemento: ElementoConviccion) -> ElementoConviccion:
        modelo = ElementoConviccionModel(
            id_caso=elemento.id_caso,
            tipo=elemento.tipo,
            descripcion=elemento.descripcion,
            archivo_url=elemento.archivo_url,
            audio_url=elemento.audio_url,
            transcripcion=elemento.transcripcion,
            boceto_redactado=elemento.boceto_redactado
        )
        db.session.add(modelo)
        db.session.commit()
        elemento.id_elemento = modelo.id_elemento
        return elemento

    def obtener_por_id(self, id_elemento: int) -> ElementoConviccion:
        e = ElementoConviccionModel.query.filter_by(id_elemento=id_elemento).first()
        if e:
            return ElementoConviccion(
                id_elemento=e.id_elemento,
                id_caso=e.id_caso,
                tipo=e.tipo,
                descripcion=e.descripcion,
                archivo_url=e.archivo_url,
                audio_url=e.audio_url,
                transcripcion=e.transcripcion,
                boceto_redactado=e.boceto_redactado
            )
        return None
