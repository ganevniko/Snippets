import smtplib
from email.mime.text import MIMEText

user=''
password=''
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(user, password)

msg = MIMEText("Testing the app")

me = "sender@domain.com"
you = "receiver@domain.com"

msg['Subject'] = 'Testing the app'
msg['From'] = me
msg['To'] = you

server.sendmail(me, [you], msg.as_string())
