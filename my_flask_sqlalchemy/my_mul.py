from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.ext.declarative import declared_attr

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/my_dom'
db = SQLAlchemy(app)

class Managerinfo(db.Model):
   __tablename__ = 'managerinfo'
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(50))
   age = db.Column(db.Integer)
   Employees = db.relationship('Manager', backref='manager')


class Engineerinfo(db.Model):
    __tablename__ = 'engineerinfo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    Employees = db.relationship('Manager', backref='engineer')


class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    type = db.Column(db.String(20))
    __mapper_args__ = {
      'polymorphic_on':type,
      'polymorphic_identity':'employee'
    }

class Manager(Employee):
    post_id = declared_attr(lambda c: db.Column(db.Integer, db.ForeignKey('managerinfo.id')))
    __mapper_args__ = {
        'polymorphic_identity':'manager'
    }


class Engineer(Employee):
    post_id = declared_attr(lambda c: db.Column(db.Integer, db.ForeignKey('engineerinfo.id')))
    __mapper_args__ = {
      'polymorphic_identity':'engineer'
    }


manager = Managerinfo(name='Manager1', age=18)
engineer = Engineerinfo(name='Engineer1', age=18)
db.session.add(manager)
db.session.add(engineer)

employee1 = Manager(name='m1', type='manager', post_id=manager.id)
employee2 = Engineer(name='e1', type='engineer', post_id=engineer.id)

db.session.add(employee1)
db.session.add(employee2)

db.session.commit()
b = 1