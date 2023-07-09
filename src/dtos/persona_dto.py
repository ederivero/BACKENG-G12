from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import Schema, fields
from models.persona import Persona


class PersonaResponseDto(SQLAlchemyAutoSchema):
    class Meta:
        model = Persona


class PersonaRequestDto(Schema):
    nombre = fields.Str(required=True)
