from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/my_dom'
db = SQLAlchemy(app)

class Managerinfo(db.Model):
   __tablename__ = 'managerinfo'
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(50))
   age = db.Column(db.Integer)


class Engineerinfo(db.Model):
    __tablename__ = 'engineerinfo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)


class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    type = db.Column(db.String(20))
    post_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    __mapper_args__ = {
      'polymorphic_on':type,
      'polymorphic_identity':'employee'
    }


class Manager(Employee):
    __mapper_args__ = {
        'polymorphic_identity':'manager'
    }

    @hybrid_property
    def manager(self):
        return Managerinfo.query.get(self.post_id)


class Engineer(Employee):
    __mapper_args__ = {
      'polymorphic_identity':'engineer'
    }

    @hybrid_property
    def engineer(self):
        return Engineerinfo.query.get(self.post_id)


manager = Managerinfo(name='Manager5', age=18)
engineer = Engineerinfo(name='Engineer5', age=18)
db.session.add(manager)
db.session.add(engineer)
db.session.flush()

employee1 = Manager(name='m5', post_id=manager.id)
employee2 = Engineer(name='e5', post_id=engineer.id)

db.session.add(employee1)
db.session.add(employee2)

db.session.commit()

employees = Employee.query.all()
ss = employees[7]
b = 1
