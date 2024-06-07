import smtplib

CORREO_ELECTRONICO = "nohemivelazco3@gmail.com"
CONTRASEÑA_CORREO = "cohxgiwhsmjhdvlq"

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(CORREO_ELECTRONICO, CONTRASEÑA_CORREO)

    asunto = "PRUEBA PYTHON"
    headers = f"From: {CORREO_ELECTRONICO}\r\nTo: {CORREO_ELECTRONICO}\r\nSubject: {asunto}"
    msg = f"{headers}\r\n\r\nHola Mundo. \r\nPrimer Correo enviado desde Python"

    smtp.sendmail(CORREO_ELECTRONICO, CORREO_ELECTRONICO, msg)