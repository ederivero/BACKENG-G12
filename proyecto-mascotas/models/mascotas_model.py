from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy import types
from base_de_datos import conexion
from enum import Enum


class SexoEnum(Enum):
    Macho = 'Macho'
    Hembra = 'Hembra'
    Otro = 'Otro'


class MascotaModel(conexion.Model):
    id = Column(autoincrement=True, type_=types.Integer, primary_key=True)
    nombre = Column(type_=types.Text, nullable=False)
    apellido = Column(type_=types.Text, nullable=True)
    sexo = Column(type_=types.Enum(SexoEnum),
                  default=SexoEnum.Otro, nullable=False)
    # name > para indicar como queremos que se llame esta columna en la base de datos, si no le ponemos este parametro su nombre sera igual que el nombre del atributo
    fechaNacimiento = Column(type_=types.Date, name='fecha_nacimiento')
    raza = Column(default='Otro', type_=types.Text)
    # relacion nuestra tabla usuarios con mascotas
    usuarioId = Column(ForeignKey(column='usuarios.id'),
                       type_=types.Integer, nullable=False, name='usuario_id')

    __tablename__ = 'mascotas'
