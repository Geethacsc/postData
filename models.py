from sqlalchemy import Integer, Column, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    yob = Column(Integer, nullable=False)
    gender = Column(String(1))
    email_id = Column(String)


