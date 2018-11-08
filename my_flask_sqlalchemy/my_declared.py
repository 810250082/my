from sqlalchemy.ext.declarative import AbstractConcreteBase
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declared_attr
db = SQLAlchemy()

class Entry(AbstractConcreteBase, db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    post_id = declared_attr(lambda c: db.Column(db.ForeignKey('post.id')))
    post = declared_attr(lambda c: db.relationship('Post', lazy='joined'))

    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()

    @declared_attr
    def __mapper_args__(self):
        return {'polymorphic_identity': self.__name__,
                'concrete': True} if self.__name__ != 'Entry' else {}


class TextEntry(Entry):
    text = db.deferred(db.Column(db.Text, nullable=False))


class PhotoEntry(Entry):
    path = db.deferred(db.Column(db.String(256), nullable=False))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    descrption = db.Column(db.Unicode(140), nullable=False)

    @classmethod
    def __declare_last__(cls):
        cls.entries = db.relationship(Entry, viewonly=True)

    def attach_entries(self, entries):
        for entry in entries:
            self.entries.append(entry)
            entry.post = self
            db.session.add(entry)



