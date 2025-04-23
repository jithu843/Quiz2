from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    department = Column(String)
    position = Column(String)
    salary = Column(Float)
    performance_score = Column(Float)

class Attendance(Base):
    __tablename__ = 'attendances'
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    date = Column(String)
    status = Column(String)
