# -*-coding: utf-8 -*-
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

class Ad(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


fun_map_dict = {}
ad_models = {}


def fun_map(fun_name):
    def decorator(func):
        fun_map_dict[fun_name] = func
        return func
    return decorator


@fun_map('__init__')
def _init(self, name=''):
    self.name = name


@fun_map('change_name')
def change_name(self, pix='sqy_'):
    """
    改变名字
    :param self:
    :return:
    """
    self.name = pix + self.name
    return True


def get_db_model(aid):

    class_name = str('Ad' + aid + 'Model')
    table_name = str('ad_' + aid)

    fun_map_dict['__tablename__'] = table_name

    if class_name not in ad_models:
        cls = type(class_name, (Ad,), fun_map_dict)
        ad_models[class_name] = cls
    return ad_models[class_name]


@app.route('/index')
def index():
    id = request.args.get('id').strip()
    name = request.args.get('name').strip()
    Model = get_db_model(id)
    obj = Model(name)
    db.session.add(obj)
    db.session.commit()
    return 'ok'


@app.route('/change')
def change():
    id = request.args.get('id').strip()
    name = request.args.get('name').strip()
    Model = get_db_model(id)
    obj = Model(name)
    obj.change_name()
    db.session.add(obj)
    db.session.commit()
    return 'ok'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)