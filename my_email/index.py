# -*- coding:utf-8 -*-
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
from email import encoders
import smtplib


# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))


def _format_addr(s):
    addr_list = s.split(',')
    new_addr_list = []
    for item in addr_list:
        name, addr = parseaddr(item)
        new_addr_list.append(formataddr((Header(name, 'utf-8').encode(), addr)))
    return ','.join(new_addr_list)


from_addr = 'm1******0@163.com'
password = "******"
to_addr = '8******2@qq.com,shitou0329@taolesoft.com'
to_addr_list = ['8******2@qq.com', 'shitou0329@taolesoft.com']

msg = MIMEText('hello sqy', 'plain', 'utf-8')
msg['Form'] = _format_addr(from_addr)
msg['To'] = _format_addr(to_addr)
msg['Subject'] = Header('FLASK API ERROR', 'utf-8').encode()


smtp_server = "smtp.163.com"
smtp_port = 25

server = smtplib.SMTP(smtp_server, smtp_port)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr_list, msg.as_string())
server.quit()