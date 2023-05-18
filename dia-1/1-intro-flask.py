from flask import Flask, request

app = Flask(__name__)

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
        return {
            'message': 'Los productos son',
            'content': productos
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


@app.route('/producto/<int:id>', methods=['GET'])
def gestionProducto(id):
    print(id)
    if request.method == 'GET':
        resultado = None
        for producto in productos:
            if producto['id'] == id:
                resultado = producto
                break

        if resultado is None:
            return {
                'message': 'No se encontro el producto a buscar'
            }

        else:
            return {
                'message': 'El producto es',
                'content': resultado
            }


if __name__ == "__main__":
    app.run(debug=True)
