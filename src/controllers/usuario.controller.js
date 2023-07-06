import { conexion } from '../base_de_datos.js'
import { registroUsuarioDto } from '../dtos/usuario.dto.js'
import bcrypt from 'bcryptjs'

export const registroUsuario = async (req, res) => {
    const { body } = req
    const dataValidada = registroUsuarioDto.validate(body)

    if (dataValidada.error) {
        return res.status(400).json({
            message: 'Error al crear el usuario',
            content: dataValidada.error.details
        })
    }

    // genera un texto aleatorio que luego se combinara con mi password y creara el hash de la password
    const salt = await bcrypt.genSalt()

    // Generamos el hash de nuestra password para almacenarla en la bd
    const password = await bcrypt.hash(dataValidada.value.password, salt)

    try {
        const usuarioCreado = await conexion.usuario.create({
            data: { ...dataValidada.value, password }
        })

        res.status(201).json({
            message: 'Usuario creado exitosamente',
            content: usuarioCreado
        })
    } catch (error) {
        return res.status(500).json({
            message: 'Error al crear el usuario',
            content: 'El usuario ya existe'
        })
    }
}