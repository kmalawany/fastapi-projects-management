from pydantic import BaseModel
from datetime import date
from typing import List


class ClientBase(BaseModel):
    name: str
    email: str
    address: str
    phone_number: str


class ProjectBase(BaseModel):
    name: str
    start_date: date
    end_date: date
    is_active: bool


class TaskBase(BaseModel):
    name: str
    start_date: date
    end_date: date
    description: str


class EmployeeBase(BaseModel):
    name: str
    email: str
    department: str
    position: str


class Employees(EmployeeBase):
    id: int
    task_id: int

    class Config:
        orm_mode = True


class Task(TaskBase):
    id: int
    project_id: int
    employee: List[Employees] = []

    class Config:
        orm_mode = True


class Project(ProjectBase):
    id: int
    client_id: int
    tasks: List[Task] = []

    class Config:
        orm_mode = True


class Client(ClientBase):
    id: int
    projects: List[Project] = []

    class Config:
        orm_mode = True



