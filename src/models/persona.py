from bd import conexion
from sqlalchemy import Column, types


class Persona(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.String, nullable=False)
    foto = Column(type_=types.String, nullable=True)
    portada = Column(type_=types.String, nullable=True)

    __tablename__ = 'personas'
