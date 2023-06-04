from flask import Flask, request
from flask_cors import CORS
from psycopg2 import connect

app = Flask(__name__)
CORS(app)

conexion = connect(database='taller', user='postgres', password='password', host='localhost')

@app.before_request
def inicializacion():
    cursor = conexion.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
        id SERIAL PRIMARY KEY, 
        email TEXT UNIQUE NOT NULL, 
        password TEXT NULL
        )""")
    cursor.close()
    print('creacion de tabla')

@app.route('/login', methods =['POST'])
def login():
    data = request.json
    print(data)
    password = data.get('password')
    email = data.get('email')
    cursor = conexion.cursor()
    print("SELECT * FROM usuarios WHERE email = '{}' AND password = '{}'".format(email, password))
    # ' OR 1=1; DROP TABLE usuarios  --
    cursor.execute("SELECT * FROM usuarios WHERE email = '{}' AND password = '{}'".format(email, password))
    resultado = cursor.fetchone()
    print(resultado)
    cursor.close()
    if not resultado:
        return {
            'message': 'Credenciales incorrectas'
        }, 403
    else:
        return {
            'message': 'Bienvenido'
        }

if __name__ == '__main__':
    app.run(debug=True)