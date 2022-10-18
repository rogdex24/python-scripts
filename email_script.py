import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = 'smtp.gmail.com'
PORT = 25

server = smtplib.SMTP(SMTP_SERVER, PORT)

server.ehlo()

# server.login('name@mail.com', 'password123') # direct

with open('password.txt', 'f') as f:
    password = f.read()

server.login('name@mail.com', password)

msg = MIMEMultipart()
msg['From'] = 'NeuralNine'
msg['To'] = 'reciever@mail.com'
msg['Subject'] = 'Just A Test'

# Message Content
with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

# Attaching Image
filename = 'photo.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

# Final Part
text = msg.as_string()
server.sendmail('sender@mail.com', 'receiver@mail.com', text)

"""
Source:
https://www.youtube.com/watch?v=FGdiSJakIS4
"""