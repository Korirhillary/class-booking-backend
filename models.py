
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Text,Integer,VARCHAR, ForeignKey

Base = declarative_base()

class Lecturehall(Base):
    __tablename__ = "lecturehalls"

    id = Column(Integer(), primary_key=True)
    Title = Column(Text(), nullable=False)
    image= Column(VARCHAR, nullable=False)
    description = Column(Text(), nullable=False)
    Price = Column(Text(), nullable=False)
    
    user = relationship ("Booking", backref = "lecturehall")

class User(Base):
        __tablename__ = "users"
        id = Column(Integer(), primary_key=True)
        first_name = Column(Text(), nullable=False)
        last_name = Column(Text(), nullable=False)
        phone_number = Column(Text(), nullable=False)
        date = Column(Text(), nullable=False)

        booklecturehalls = relationship("Booklecturehall",backref = "user")

class Booklecturehall(Base):
      __tablename__ = "booklecturehalls"

      id = Column(Integer(), primary_key=True)
      lecturehall_id = Column(Integer(), ForeignKey('lecturehalls.id'))
      lecturehall_id = Column(Integer(), ForeignKey('users.id'))


    

