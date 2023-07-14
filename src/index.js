import express from "express";

const servidor = express();
const PORT = process.env.PORT ?? 3000;

servidor.get("/", (req, res) => {
  return res.status(200).json({
    message: "Bienvenido a mi API con MongoDb",
  });
});

servidor.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});
