from start import db
import time


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    status = db.Column(db.Integer, default=1)
    created_time = db.Column(db.Integer, default=time.time())
    updated_time = db.Column(db.Integer, default=time.time())
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __init__(self, name):
        self.name = name
