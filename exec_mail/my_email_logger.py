import logging
from logging.handlers import SMTPHandler



class Mail(object):
    def __init__(self):
        email_logger = logging.getLogger('sqy')
        email_handler = SMTPHandler(("smtp.163.com", 25),
                                    "m1******0@163.com",
                                    ['8******2@qq.com'],
                                    'FLASK API ERROR',
                                    credentials=("m1******0@163.com", "******"))
        email_logger.addHandler(email_handler)
        self.email_logger = email_logger

    def send(self, exc_info=None):
        self.email_logger.warning('api error', exc_info=exc_info)