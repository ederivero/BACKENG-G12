from flask_restful import Resource
from base_de_datos import conexion
from models.usuarios_model import UsuarioModel


class UsuariosController(Resource):
    # cuando yo heredo la clase Resource ahora los metodos que yo cree con el mismo nombre que un metodo HTTP (GET, POST, PUT, DELETE) entonces ingresaran a esos metodos

    def get(self):
        resultado = conexion.session.query(UsuarioModel).all()
        print(resultado)
        return {
            'message': 'me hicieron get!'
        }

    def post(self):
        # inicializo mi nuevo usuario
        nuevoUsuario = UsuarioModel(
            nombre='Eduardo', apellido='de Rivero', correo='ederiveroman@gmail.com', dni='73546796')
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
            return {
                'message': 'Erro al crear el usuario',
                'content': error.args  # args > argumentos (porque fallo)
            }, 400  # bad request (mala solicitud por parte del cliente)
