import * as UsuarioController from '../controllers/usuario.controller.js'
import { Router } from 'express'

// Utilizamos la interfaz de express del enrutador
export const usuarioRouter = Router()


// Creamos nuestra ruta del registro
usuarioRouter.post('/registro', UsuarioController.registroUsuario)