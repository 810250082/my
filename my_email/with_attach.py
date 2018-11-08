# -*- coding:utf-8 -*-
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email.utils import parseaddr, formataddr
from email import encoders
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = 'm1******0@163.com'
password = "******"
to_addr = '8******2@qq.com'

msg = MIMEMultipart()
msg['Form'] = _format_addr(from_addr)
msg['To'] = _format_addr(to_addr)
msg['Subject'] = Header('FLASK API ERROR', 'utf-8').encode()

msg.attach(MIMEText('hello sqy with accessory', 'plain', 'utf-8'))

with open('./medal_week.png', 'rb') as f:
    mime = MIMEBase('image', 'png', filename='test.png')

    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')

    mime.set_payload(f.read())

    encoders.encode_base64(mime)

    msg.attach(mime)



smtp_server = "smtp.163.com"
smtp_port = 25

server = smtplib.SMTP(smtp_server, smtp_port)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()