import smtplib
import mimetypes
from email.message import EmailMessage
from email.utils import formataddr

CORREO_ELECTRONICO = "nohemivelazco3@gmail.com"
CONTRASEÑA_CORREO = "cohxgiwhsmjhdvlq"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_SSL_PORT = 465

def main():
    enviarCorreoSimple()
    enviarAdjuntos()

def enviarCorreoSimple():
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(CORREO_ELECTRONICO, CONTRASEÑA_CORREO)

            asunto = "PRUEBA PYTHON"
            msg = EmailMessage()
            msg["From"] = CORREO_ELECTRONICO
            msg["To"] = CORREO_ELECTRONICO
            msg["Subject"] = asunto
            msg.set_content("Hola Mundo.\nPrimer Correo enviado desde Python")

            smtp.send_message(msg)
            print("Correo simple enviado exitosamente.")
    except Exception as e:
        print(f"Error al enviar correo simple: {e}")

def enviarAdjuntos():
    file_name = "imagenPruba.jpg" 
    file_path = "C:/Users/Dell/OneDrive/Documentos/Automatization-Scripts/Sending-Email/imagenPruba.jpg"
    
    try:
        with open(file_path, "rb") as f:
            file_data = f.read()
        
        file_type, _ = mimetypes.guess_type(file_name)
        main_type, sub_type = file_type.split('/')

        msg = EmailMessage()
        msg["Subject"] = "Test Email with Image Attachment"
        msg["From"] = CORREO_ELECTRONICO
        msg["To"] = "a20490742@itmexicali.edu.mx"
        msg.set_content("Hello, this is a test email with an image attachment.")

        msg.add_attachment(file_data, maintype=main_type, subtype=sub_type, filename=file_name)

        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_SSL_PORT) as smtp:
            smtp.login(CORREO_ELECTRONICO, CONTRASEÑA_CORREO)
            smtp.send_message(msg)
            print("Correo con adjunto enviado exitosamente.")
    except FileNotFoundError:
        print(f"Archivo no encontrado: {file_path}")
    except Exception as e:
        print(f"Error al enviar correo con adjunto: {e}")

if __name__ == "__main__":
    main()