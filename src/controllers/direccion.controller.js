import { conexion } from '../base_de_datos.js'
import { direccionDto } from '../dtos/direccion.dto.js'
import { validarData } from '../utils/validador.js'
import { Prisma } from '@prisma/client'

export const crearDireccion = async (req, res) => {
    // req.user > usuario
    const { body, user } = req

    const dataValidada = direccionDto.validate(body)

    try {
        const data = validarData({ error: dataValidada.error, data: dataValidada.value, message: 'Error al crear el departamento' })
        const direccionCreada = await conexion.direccion.create({ data: { ...data, usuarioId: user.id } })

        return res.status(201).json({
            message: 'Direccion creada exitosamente',
            content: direccionCreada
        })

    } catch (error) {
        if (error instanceof Prisma.PrismaClientKnownRequestError) {
            return res.status(500).json({
                message: 'Error al crear el departamento',
                content: error.message
            })
        }
        else {
            return res.status(400).json(JSON.parse(error.message))
        }
    }
}