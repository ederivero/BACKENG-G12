from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://localhost:5500', 'http://127.0.0.1:5500'], methods=['GET', 'POST', 'PUT', 'DELETE'])

productos = [{
    'id': 1,
    'nombre': 'Martillo',
    'precio': 15.8,
    'disponible': True
},
    {
    'id': 2,
    'nombre': 'Serrucho',
    'precio': 20.5,
    'disponible': True
},
    {
    'id': 3,
    'nombre': 'Taladro',
    'precio': 120.0,
    'disponible': False

}]


@app.route('/productos', methods=['GET', 'POST'])
def gestionProductos():
    # request > me da toda la informacion de mi cliente
    print(request.method)
    if request.method == 'GET':
        productos_existentes = []
        for producto in productos:
            if producto is None:
                # evita que el codigo de a continuacion no se ejecute por este ciclo
                continue
            productos_existentes.append(producto)

        return {
            'message': 'Los productos son',
            'content': productos_existentes
        }
    elif request.method == 'POST':
        print(request.json)
        id = len(productos) + 1
        data = request.json
        # crea una nueva llave llamada id si no existe, pero si existe, reemplazara su valor
        data['id'] = id
        productos.append(data)

        return {
            'message': 'Producto creado exitosamente'
        }


@app.route('/producto/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def gestionProducto(id):
    print(id)
    resultado = None
    for producto in productos:
        if producto is None:
            continue
        if producto['id'] == id:
            resultado = producto
            break

    if resultado is None:
        return {
            'message': 'No se encontro el producto a buscar'
        }

    if request.method == 'GET':
        return {
            'message': 'El producto es',
            'content': resultado
        }

    elif request.method == 'PUT':
        data = request.json
        # la posicion sera el valor del id - 1 porque cuando la pos es 0 el id es 1 y asi sucesivamente
        productos[id - 1] = data
        # el primer corchete indicara la posicion de la lista y el segundo corchete indicara la propiedad del diccionario
        productos[id - 1]['id'] = id
        return {
            'message': 'Producto actualizado exitosamente'
        }

    elif request.method == 'DELETE':
        productos[id - 1] = None

        return {
            'message': 'Producto eliminado exitosamente'
        }


if __name__ == "__main__":
    app.run(debug=True)
