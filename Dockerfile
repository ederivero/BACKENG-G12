# aca tiene que ir la imagen que la buscaremos en el docker hub
FROM node:20-alpine3.17

# declaramos las variables de entorno para utilizar en esta imagen
ENV PORT=8000
ENV NOMBRE=Eduardo

# que la imagen almacene de manera mas facil los archivos del proyecto porque al indicar la ubicacion del directorio de trabajo creara una carpeta en la imagen donde guaradara todos los archivos copiados
WORKDIR /app

# ahora copiamos los archivos locales a nuestra imagen
# el nombre del archivo o directorio | en donde o como se llamara en la imagen
COPY package.json package.json

# o tbn se puede copiar de la siguiente manera
# las primeras posiciones seran los archivos a copiar y la ultima posicion hacia donde se va a copiar, no es necesario volver a poner '/app' ya que ese sera el directorio por defecto
COPY ["package-lock.json", ".", "./"]

# se usa para instalar las librerias
# --production > sirve para solamente instalar las dependencias y no las de desarrollo
RUN npm install --production

CMD ["npm", "start"]