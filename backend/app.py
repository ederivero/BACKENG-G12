from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, types
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password@localhost:5432/taller2'
conexion = SQLAlchemy(app)

class Usuario(conexion.Model):
    id = Column(type_=types.Integer, primary_key= True, autoincrement=True)
    email = Column(type_=types.Text, unique=True, nullable=False)
    password = Column(type_=types.Text, nullable=True)
    __tablename__ ='usuarios'

Migrate(app, conexion)

@app.route('/login', methods= ['POST'])
def login():
    data = request.json
    result = conexion.session.query(Usuario).filter_by(
        email = data.get('email'), password = data.get('password')).all()

    if not result:
        return {
            'message': 'credenciales incorrectas'
        }, 403
    else:
        return {
            'message':'bienvenido'
        }, 200

if __name__ == '__main__':
    app.run(debug=True)