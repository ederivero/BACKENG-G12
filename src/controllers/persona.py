# pip install flask-restful
from flask_restful import Resource, request
from models.persona import Persona
from bd import conexion
from dtos.persona_dto import PersonaResponseDto, PersonaRequestDto
from os import path, getcwd
from werkzeug.utils import secure_filename
from uuid import uuid4
from os import environ
from boto3 import Session

AWSSession = Session(aws_access_key_id=environ.get('AWS_ACCESS_KEY'),
                     aws_secret_access_key=environ.get('AWS_SECRET_KEY'),
                     region_name=environ.get('AWS_BUCKET_REGION'))


class PersonasController(Resource):
    def get(self):
        personas = conexion.session.query(Persona).all()
        S3 = AWSSession.client('s3')

        # convierte las instancias a diccionarios y si le pasamos el parametro many=True converta un arreglo de instancias a un arreglo de diccionarios para que el cliente (frontend) lo pueda entender
        data = PersonaResponseDto().dump(personas, many=True)

        for persona in data:
            if persona.get('foto'):
                persona['foto'] = S3.generate_presigned_url('get_object',
                                                            Params={
                                                                'Bucket': environ.get('AWS_BUCKET_NAME'),
                                                                'Key': persona.get('foto')},
                                                            ExpiresIn=50)
            if persona.get('portada'):
                persona['portada'] = S3.generate_presigned_url('get_object',
                                                               Params={
                                                                   'Bucket': environ.get('AWS_BUCKET_NAME'),
                                                                   'Key': persona.get('portada')},
                                                               ExpiresIn=50)  # en segundos

        return {
            'content': data
        }

    def post(self):
        print(request.form)
        print(request.files)
        foto = request.files.get('foto')
        portada = request.files.get('portada')
        # cwd > current working directory
        directorioActual = getcwd()
        S3 = AWSSession.client('s3')
        try:
            dataValidada = PersonaRequestDto().load(request.form)
            print(dataValidada)
            nombreFoto = None
            nombrePortada = None
            if foto:
                # secure_filename > quita caracteres que puedan poder en riesgo la lectura de los archivos, quita slash, caracteres invisibles y puntos
                filename = secure_filename(foto.filename)
                nombreFoto = f'{uuid4()}-{filename}'
                ruta = path.join(directorioActual, 'imagenes', nombreFoto)
                foto.save(ruta)

                S3.upload_file(
                    ruta, environ.get('AWS_BUCKET_NAME'), nombreFoto)

            if portada:
                filename = secure_filename(portada.filename)
                nombrePortada = f'{uuid4()}-{filename}'
                ruta = path.join(directorioActual, 'imagenes', nombrePortada)
                portada.save(ruta)
                S3.upload_file(ruta, environ.get(
                    'AWS_BUCKET_NAME'), nombrePortada)

            nuevaPersona = Persona(nombre=dataValidada.get('nombre'),
                                   foto=nombreFoto, portada=nombrePortada)

            conexion.session.add(nuevaPersona)
            conexion.session.commit()

            return {
                'message': 'Persona creada exitosamente'
            }, 201

        except Exception as e:
            return {
                'message': 'Error al crear la persona',
                'content': e.args
            }


class PersonaController(Resource):
    def delete(self, id):
        personaEncontrada = conexion.session.query(Persona).filter_by(id=id).first()
        if not personaEncontrada:
            return {
                'message': 'Persona no existe'
            }
        
        S3 = AWSSession.client('s3')
        if personaEncontrada.foto:
            S3.delete_object(Bucket=environ.get('AWS_BUCKET_NAME'), Key= personaEncontrada.foto)
        
        if personaEncontrada.portada:
            S3.delete_object(Bucket=environ.get('AWS_BUCKET_NAME'), Key= personaEncontrada.portada)

        conexion.session.query(Persona).filter_by(id=id).delete()

        conexion.session.commit()

        return {
            'message': 'Persona eliminada de la base de datos'
        }