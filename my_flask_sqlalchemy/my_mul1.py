from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.ext.declarative import declared_attr

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/my_dom'
db = SQLAlchemy(app)


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
    __mapper_args__ = {
        'polymorphic_identity':'manager'
    }


class Engineer(Employee):
    __mapper_args__ = {
      'polymorphic_identity':'engineer'
    }

all_data = Employee.query.all()
b = 1
# manager = Managerinfo(name='Manager1', age=18)
# engineer = Engineerinfo(name='Engineer1', age=18)
# db.session.add(manager)
# db.session.add(engineer)
#
# Manager(name='www1', type='manager')
#
# db.session.add(employee1)
# db.session.add(engineer1)

# db.session.commit()
b = 1