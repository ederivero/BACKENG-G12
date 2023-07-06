import Prisma from "@prisma/client"

// variable encargada de conectarse a la base de datos y por aca haremos todas las consultas
export const conexion = new Prisma.PrismaClient()