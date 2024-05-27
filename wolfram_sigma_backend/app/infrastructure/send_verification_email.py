import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import mail_address, mail_password


def send_verification_email(email: str, verification_token: str):
    sender_email = mail_address
    password = mail_password
    receiver_email = email

    # Создаем сообщение
    message = MIMEMultipart("alternative")
    message["Subject"] = "Verify your email"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Создаем URL для верификации
    verification_url = f"http://127.0.0.1:4200/verify?token={verification_token}"

    # Текст сообщения
    text = f"Please verify your email by clicking on the following link: {verification_url}"
    part = MIMEText(text, "plain")
    message.attach(part)

    # Отправка сообщения через SMTP сервер
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")
