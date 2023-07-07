import Joi from 'joi'

export const direccionDto = Joi.object({
    calle: Joi.string().required(),
    // si solo queremos validar y convertir a un numero usamos number() 
    // pero si queremos que solo sea entero (no decimal) usamos adiciona la validacion integer()
    numero: Joi.number().integer().required(),
    referencia: Joi.string(),
    departamento: Joi.string()
})