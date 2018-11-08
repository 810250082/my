# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column
from sqlalchemy.types import String, Integer, CHAR, BIGINT, Unicode, UnicodeText
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy.ext.associationproxy import association_proxy

Engine = create_engine('mysql+pymysql://root:root@localhost/my_dom?charset=utf8', encoding='utf-8', echo=True)
Session = sessionmaker(Engine)

class BaseModel(declarative_base()):
    __abstract__ = True

class Entity(BaseModel):
    __tablename__ = 'entity'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Unicode(32), server_default='')

    _attributes = relationship('Attribute',
                               collection_class=attribute_mapped_collection('key'),
                               lazy='joined', cascade="all, delete-orphan")
    attributes = association_proxy('_attributes', 'value',
                                   creator=lambda k, v: Attribute(key=k, value=v))


class Attribute(BaseModel):
    __tablename__ = 'attribute'

    id = Column(Integer, autoincrement=True, primary_key=True)
    entity = Column(Integer, ForeignKey('entity.id'), index=True)
    key = Column(Unicode(32), server_default='')
    value = Column(UnicodeText)


if __name__ == '__main__':
    BaseModel.metadata.create_all(Engine)

    session = Session()

    entity = Entity(name=u'哈哈')
    entity.attributes[u'first'] = u'abc'
    entity.attributes[u'sec'] = u'hoho'
    session.add(entity)
    session.commit()

    entity = session.query(Entity).first()
    print entity.attributes
    del entity.attributes['first']
    session.commit()

    entity = session.query(Entity).first()
    print entity.attributes


def init_db():
    BaseModel.metadata.create_all(Engine)

def drop_db():
    BaseModel.metadata.drop_all(Engine)


# if __name__ == '__main__':
#     init_db()
#     # drop_db()
#     #BaseModel.metadata.tables['user'].create(Engine, checkfirst=True)
#     #BaseModel.metadata.tables['user'].drop(Engine, checkfirst=False)
#     pass