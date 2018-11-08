from sqlalchemy import Column , String , create_engine ,ForeignKey
from sqlalchemy.orm import sessionmaker ,relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    books = relationship('Book')
class Book(Base):
    __tablename__ = 'book'
    id = Column(String(20) , primary_key=True)
    name = Column(String(20))
    stu_id = Column(String(20) ,ceignKey('student.id'))

engine = create_engine('mysql+pymysql://root:root@localhost:3306/mytest')

DBSession = sessionmaker(bind=engine)

session = DBSession()

book1 = Book(id='1' , name='math' ,stu_id='1')
book2 = Book(id='2' , name='englisth' ,stu_id='1')
session.add(book1)
session.add(book2)
session.commit()
stuInfo = session.query(Student).filter(Student.id==1).one()
session.close()




#new_stu = Student(id='1' , name='sqy')
#session.add(new_stu)
#session.commit()
#session.close()

#get data
#stu = session.query(Student).filter(Student.id=='1').one()
#print('type:' , type(stu))
#print('name:' , stu.name)
#session.close()

