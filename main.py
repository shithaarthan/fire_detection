import socket
import smtplib
from email.message import EmailMessage
import data


def fireThreatMsg():
    Message = EmailMessage()
    
    #message contents
    Message["subject"] = "fire threat !"
    Message["From"] = data.from_mail
    Message["To"] = data.to_mail
    Message.set_content("There is a fire zone detected at your building, this is an autogenerated message. Do not reply")
    
    # to establish secure connection
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login(data.from_mail,data.app_password)

    server.send_message(Message)
    print("mail sent and server has been closed .")
    server.quit()