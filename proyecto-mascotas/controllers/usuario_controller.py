from flask_restful import Resource, request
from base_de_datos import conexion
from models.usuarios_model import UsuarioModel
from dtos.usuario_dto import UsuarioResponseDto, UsuarioRequestDto


class UsuariosController(Resource):
    # cuando yo heredo la clase Resource ahora los metodos que yo cree con el mismo nombre que un metodo HTTP (GET, POST, PUT, DELETE) entonces ingresaran a esos metodos

    def get(self):
        # Lista
        resultado = conexion.session.query(UsuarioModel).all()
        # many = True > el dto iterara el arreglo o lista y convertira cada uno de ellos
        dto = UsuarioResponseDto(many=True)
        # dump > convierte la instancia de la clase en un diccionario
        data = dto.dump(resultado)
        # data = []
        # for usuario in resultado:
        #     data.append({
        #         'id': usuario.id,
        #         'nombre': usuario.nombre,
        #         'apellido': usuario.apellido,
        #         'correo': usuario.correo,
        #         'dni': usuario.dni
        #     })
        return {
            'content': data
        }

    def post(self):
        data = request.json
        dto = UsuarioRequestDto()
        # load > valida el diccionario que le pasamos con los campos que cumplan las condiciones (requeridos, que sean del tipo de dato correcto)
        dataValidada = dto.load(data)
        print(dataValidada)
        # inicializo mi nuevo usuario
        nuevoUsuario = UsuarioModel(**dataValidada)
        # nuevoUsuario = UsuarioModel(nombre = dataValidada.get('nombre'), apellido = dataValidada.get('apellido'), ...)
        # indicar que vamos a agregar un nuevo registro
        # https://docs.sqlalchemy.org/en/20/orm/session_basics.html#adding-new-or-existing-items
        conexion.session.add(nuevoUsuario)
        try:
            # se usa para transacciot sirve para indicar que todos los cambios se guarden de manera permanente, sino hacemos el commit entonces no se guardara la informacion de manera permanente
            conexion.session.commit()
            return {
                'message': 'Usuario creado exitosamente'
            }, 201  # Created (Creado exitosamente)
        except Exception as error:
            # rollback > para retroceder y dejar todos los posibles cambios sin efecto (los incrementadores, nuevos registros, actualizaciones y eliminaciones) quedan sin efecto
            # https://docs.sqlalchemy.org/en/20/orm/session_basics.html#rolling-back
            conexion.session.rollback()
            return {
                'message': 'Erro al crear el usuario',
                'content': error.args  # args > argumentos (porque fallo)
            }, 400  # bad request (mala solicitud por parte del cliente)
