import { conexion } from '../base_de_datos.js'
import fs from 'fs' // file system
import path from 'path'
import { fileURLToPath } from 'url';

export const crearProducto = async (req, res) => {
    const { body, file } = req
    console.log(body)
    console.log(file)

    return res.json({
        message: 'Producto creado exitosamente'
    })
}

export const devolverImagenLocal = async (req, res) => {
    const { nombre } = req.params

    try {
        const __filename = fileURLToPath(import.meta.url);
        const __dirname = path.dirname(__filename);
        // leemos el archivo para ver si existe, si no existe emitira un error
        const ubicacion = path.join(__dirname, '../../imagenes', nombre)
        fs.readFileSync(ubicacion)

        return res.sendFile(ubicacion)
    } catch (error) {
        return res.status(404).json({
            message: 'El archivo no existe',
            content: error.message
        })
    }

}