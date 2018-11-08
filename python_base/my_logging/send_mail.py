# -*- coding:utf8 -*-
from flask import Flask
from flask_mail import Mail, Message



app = Flask(__name__)
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.163.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'm1******0@163.com',
    MAIL_PASSWORD = '******',
    MAIL_DEFAULT_SENDER = 'm1******0@163.com'
))

mail = Mail(app)

@app.route('/')
def index():
    msg = Message("EmailTest" ,recipients=['8******2@qq.com'])
    msg.body = "Hello World! This  Email from Web"
    mail.send(msg)
    return '<h3>Sended  email to U! ^^</h3>'

@app.route('/logging/mail')
def mail():
    logging.handlers.S



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
