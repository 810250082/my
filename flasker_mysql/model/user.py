from start import db
import time


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    status = db.Column(db.Integer, default=1)
    created_time = db.Column(db.Integer, default=time.time())
    updated_time = db.Column(db.Integer, default=time.time())

    def __repr__(self):
        return "<User %r>" % self.username

    def __init__(self, username='', role_id=1):
        self.username = username
        self.role_id = role_id
