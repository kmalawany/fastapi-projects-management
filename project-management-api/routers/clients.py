from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from database.database import get_db
from routers.schemas import ClientBase, Project
from database import clients_db, projects_db

router = APIRouter(prefix='/clients', tags=['Clients Operations'])


@router.post('')
def create_client(request: ClientBase, db: Session = Depends(get_db)):
    return clients_db.add(db, request)


@router.get('/all')
def get_all_clients(db: Session = Depends(get_db)):
    return clients_db.get_all(db)


@router.get('/{id}')
def get_client(id: int, db: Session = Depends(get_db)):
    return clients_db.get_client(db, id)


@router.delete('')
def delete_client(id: int, db: Session = Depends(get_db)):
    return clients_db.delete_client(db, id)



