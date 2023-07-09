# librerias
from flask import Flask
from dotenv import load_dotenv
from flask_migrate import Migrate
from os import environ
from flask_restful import Api
# archivos
from bd import conexion
from controllers.persona import PersonasController, PersonaController

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
api = Api(app)

conexion.init_app(app)

Migrate(app, conexion)

# agrego las rutas
api.add_resource(PersonasController, '/personas')
api.add_resource(PersonaController, '/persona/<int:id>')

if __name__ == "__main__":
    app.run(debug=True)
