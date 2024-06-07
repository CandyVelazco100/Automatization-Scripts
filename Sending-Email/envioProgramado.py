import smtplib
import schedule
import time

# Configuración del correo electrónico
CORREO_ELECTRONICO = "nohemivelazco3@gmail.com"
CONTRASEÑA_CORREO = "cohxgiwhsmjhdvlq"

def enviar_correo():
    # Conexión con el servidor SMTP de Gmail
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        # Autenticación con el correo electrónico y contraseña
        smtp.login(CORREO_ELECTRONICO, CONTRASEÑA_CORREO)

        # Configuración del correo electrónico a enviar
        asunto = "PRUEBA PYTHON"
        headers = f"From: {CORREO_ELECTRONICO}\r\nTo: {CORREO_ELECTRONICO}\r\nSubject: {asunto}"
        msg = f"{headers}\r\n\r\nHola Mundo. \r\nPrimer Correo enviado desde Python"

        # Envío del correo electrónico
        smtp.sendmail(CORREO_ELECTRONICO, CORREO_ELECTRONICO, msg)

schedule.every().day.at("07:30").do(enviar_correo) 

while True:
    schedule.run_pending()
    time.sleep(1)