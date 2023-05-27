from models.mascotas_model import MascotaModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class MascotaRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = MascotaModel
        # indicamos al DTO que tambien haga la validacion de las columnas que sean llaves foraneas
        include_fk = True
