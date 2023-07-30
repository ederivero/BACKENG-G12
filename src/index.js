import express from 'express'
import mongoose from 'mongoose'
import { Producto } from './models/productos.js'

const servidor = express()
const PORT = process.env.PORT ?? 3000

servidor.get('/', (req, res) => {
  return res.status(200).json({
    message: 'Bienvenido a mi API con MongoDb',
    content: new Date().toISOString(),
  })
})

servidor.listen(PORT, async () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`)
  await mongoose.connect(process.env.DATABASE_URL)
  console.log('Base de datos conectada exitosamente')
})
