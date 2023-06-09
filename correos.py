from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# MIME > Multipurpose Internet Mail Extensions
from smtplib import SMTP
# SMTP > Simple Mail Transfer Protocol


def enviarCorreo():
    mensaje = MIMEMultipart()
    # Titulo del correo
    mensaje['Subject'] = 'Olvidaste la password'
    # Emisor del correo
    mensaje['From'] = 'ederiveroman@gmail.com'
    # Destinatario del correo
    mensaje['To'] = 'eduardomanrique@ravn.co'

    # Cuerpo del correo
    body = 'Hola, buenos dias. Al paracer has olvidado tu contrasena, te sugerimos que la cambies en el siguiente link'

    texto = MIMEText(body, 'plain')

    mensaje.attach(texto)

    # Inicio la conexion con mi cuenta de GMAIL
    conexion = SMTP('smtp.gmail.com', 587)

    conexion.starttls()

    # me autentico con mis credenciales
    conexion.login('ederiveroman@gmail.com', 'zffzooxyeqbfxpig')

    # envio el correo hacia los destinatarios
    conexion.sendmail(from_addr='ederiveroman@gmail.com',
                      to_addrs='eduardomanrique@ravn.co', msg=mensaje.as_string())

    # finalizo la conexion con el servidor de correos
    conexion.quit()

    print('Email enviado exitosamente')


enviarCorreo()
