import express from 'express';
import Joi from 'joi';

const servidor = express();
const productos = [];
// lo que nos llegara a este validador sera un objeto (JSON)
const productoValidator = Joi.object({
    // El metodo message sirve para modificar el mensaje de error de la ultima validacion, esto no aplica para la validacion de 'required' 
    nombre: Joi.string().required().min(5).message('La longitud minima es de 5'),
    precio: Joi.number().min(0).required(),
    descripcion: Joi.string().optional()
});

// indicar middlewares (intermediario) 
// ahora nuestra aplicacion entendera y convertira la informacion entrante que sea de tipo JSON (application/json)
servidor.use(express.json())
// tipo form-urlencoded (application/form-url-encoded)
// servidor.use(express.urlencoded())

servidor.get('/inicio', (req, res) => {
    res.status(200).json({
        message: 'Bienvenido a mi API en Express'
    })
})

servidor.route('/productos').post((req, res) => {
    console.log(req.body);
    // const body = req.body
    const { body } = req;

    const validacion = productoValidator.validate(body);
    console.log(validacion);

    if (validacion.error) {
        return res.status(400).json({
            message: 'Error al crear el producto',
            content: validacion.error.details
        })
    }
    else {
        productos.push(validacion.value);
        return res.status(201).json({
            message: 'Producto creado exitosamente'
        })
    }
}).get((req, res) => {
    res.json({
        content: productos
    })
})

servidor.route('/producto/:id').get((req, res) => {
    console.log(req.params)
    const { id } = req.params
    const resultado = productos[id]
    console.log(resultado)
    if (!resultado) {
        return res.status(404).json({
            message: 'El producto no existe'
        })
    } else {
        return res.json({
            content: resultado
        })
    }
}).put((req, res) => {
    const id = req.params.id
    const body = req.body
    const productoEncontrado = productos[id]

    if (!productoEncontrado) {
        return res.status(404).json({
            message: 'El producto no existe'
        })
    }

    // si es que existe el producto
    const validacion = productoValidator.validate(body)

    if (validacion.error) {
        return res.status(400).json({
            message: 'Error al actualizar el producto',
            content: validacion.error.details
        })
    } else {
        productos[id] = validacion.value

        return res.json({
            message: 'Producto actualizado exitosamente'
        })
    }
}).delete((req, res) => {
    const { id } = req.params

    // primero validar si el producto existe
    // si no existe, retornar que el producto no existe
    const productoEncontrado = productos[id]
    if (!productoEncontrado) {
        return res.status(404).json({
            message: 'El producto no existe'
        })
    }


    // si existe cambiar su valor de la posicion a null
    productos[id] = null

    // retornar el mensaje
    return res.json({
        message: 'Producto eliminado exitosamente'
    })
})

servidor.listen(3000, () => {
    console.log('Servidor corriendo exitosamente')
});