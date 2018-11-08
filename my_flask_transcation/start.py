from flask import Flask
from ext import db
from models import User

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)


@app.route('/')
def index():
    return 'hello world!'


@app.route('/add')
def add_dom():
    user4 = User('sqy1', 4)
    user5 = User('sqy2', 5)
    user3 = User('sqy3', 1)
    db.session.add(user4)
    db.session.add(user5)
    db.session.begin_nested()
    db.session.add(user3)
    db.session.rollback()
    db.session.commit()
    return 'ok'


@app.route('/merge')
def merge_dom():
    user1 = User.query.get(1)
    new_user = User('new_user', 2)
    new_user.id = 1
    db.session.merge(new_user)
    db.session.flush()
    db.session.commit()
    return 'ok'


@app.route('/back')
def back_dom():
    user1 = User.query.get(1)
    user1.username = 'sqy1'
    user1.type = 1
    db.session.add(user1)
    db.session.commit()
    db.session.rollback()
    return 'ok'





if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
