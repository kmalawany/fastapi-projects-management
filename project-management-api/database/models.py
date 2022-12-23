from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Projects(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    is_active = Column(Boolean, default=True)
    client_id = Column(Integer, ForeignKey('clients.id'))

    tasks = relationship('Tasks', back_populates='project')
    client = relationship('Client', back_populates='project')


class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, index=True, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    name = Column(String, unique=True)
    start_date = Column(Date)
    end_date = Column(Date)
    description = Column(String)

    project = relationship('Projects', back_populates='tasks')


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, index=True, primary_key=True)
    client_name = Column(String)
    email = Column(String)
    address = Column(String)
    phone_number = Column(String)

    project = relationship('Projects', back_populates='client')


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, index=True, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    department = Column(String)
    position = Column(String)
