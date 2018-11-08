# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Addres(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(50))
    user_id = db.Column(db.ForeignKey(u'user.id'), index=True)
    created_time = db.Column(db.DateTime)

    user = db.relationship(u'User', primaryjoin='Addres.user_id == User.id', backref=u'address')


class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    type = db.Column(db.Integer)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    type = db.Column(db.Integer)
