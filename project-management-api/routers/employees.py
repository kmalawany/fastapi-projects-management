from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm.session import Session
from database.database import get_db
from database import employee_db
from routers.schemas import Employees, EmployeeBase

router = APIRouter(prefix='/employee', tags=['Employee Operations'])


@router.post('/add')
def add_employee(request: EmployeeBase, db: Session = Depends(get_db)):
    return employee_db.add_employee(db, request)


@router.get('/{id}')
def get_employee(id: int, db: Session = Depends(get_db)):
    return employee_db.get_employee(id, db)


@router.get('/all/')
def get_all(db: Session = Depends(get_db), skip: int = 0, limit: int = Query(default=5, le=5)):
    return employee_db.get_all(db, skip, limit)


@router.delete('/delete/{id}')
def delete_employee(id: int, db: Session = Depends(get_db)):
    return employee_db.delete_employee(id, db)

