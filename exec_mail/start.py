from flask import Flask, request
import config
import sys
from my_email_logger import Mail
# import logging
# from logging.handlers import SMTPHandler
#
# email_logger = logging.getLogger('sqy')
# email_handler = SMTPHandler(("smtp.163.com", 25),
#                             "m1******0@163.com",
#                             ['8******2@qq.com'],
#                             'FLASK API ERROR',
#                             credentials=("m1******0@163.com", "******"))
# email_logger.addHandler(email_handler)

app = Flask(__name__)
# app.config.from_object('config')


@app.route('/index', methods=['GET', 'POST'])
def index():
    a = 1/0
    return 'ok'


@app.errorhandler(Exception)
def handler_error(e):
    exc_type, exc_value, tb = sys.exc_info()
    assert exc_value is e
    Mail().send(exc_info=(exc_type, exc_value, tb))
    return 'send error-mail over'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
