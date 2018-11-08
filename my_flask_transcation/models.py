from ext import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    type = db.Column(db.Integer, default=1)
    start = db.Column(db.Integer)
    end = db.Column(db.Integer)
    addresses = db.relationship('Address', backref='user')

    def __init__(self, username, type):
        self.username = username
        self.type = type



class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(50))
    created_time = db.Column(db.DATETIME)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, email_address):
        self.email_address = email_address


class Company(db.Model):
    id = db.Column(db.SmallInteger, primary_key=True)
    name = db.Column(db.String(50))
    type = db.Column(db.Integer, default=0)


class Error(db.Model):
    __bind_key__ = 'my_dom'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


class School(db.Model):
    __tablename__ = 'school'
    __bind_key__ = 'my_dom'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    addr = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    teachers = db.relationship('Teacher', backref='shool', lazy='dynamic')


class Teacher(db.Model):
    __tablename__ = 'teacher'
    __bind_key__ = 'my_dom'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'))