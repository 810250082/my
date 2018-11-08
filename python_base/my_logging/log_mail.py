import logging
from logging.handlers import SMTPHandler

errlog = logging.getLogger()
sh = SMTPHandler(('smtp.163.com', 25), 'm1******0@163.com', ['8******2@qq.com'], 'logging error', ('m1******0@163.com', '******'))
errlog.addHandler(sh)

try:
    a = 1 / 0
except:
    errlog