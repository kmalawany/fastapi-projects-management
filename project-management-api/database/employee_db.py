from routers.schemas import EmployeeBase
from sqlalchemy.orm.session import Session
from database.models import Employee
from fastapi import status, HTTPException


def add_employee(db: Session, request: EmployeeBase, task_id: int = None):
    employee = Employee(
        name=request.name,
        email=request.email,
        department=request.department,
        position=request.position,
        task_id=task_id
    )
    db.add(employee)
    db.commit()
    db.refresh(employee)

    return employee


def get_employee(id: int, db: Session):
    employee = db.query(Employee).filter(Employee.id == id).first()

    if employee is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Employee not found')
    else:
        return employee


def get_all(db: Session, skip: int = 0, limit: int = 5):
    return db.query(Employee).offset(skip).limit(limit).all()


def delete_employee(id: int, db: Session):
    employee = db.query(Employee).filter(Employee.id == id).first()

    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Employee not found')
    else:
        db.delete(employee)
        db.commit()
        return 'Employee deleted'


