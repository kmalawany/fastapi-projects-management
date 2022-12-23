from routers.schemas import ClientBase
from sqlalchemy.orm.session import Session
from database.models import Client
from fastapi import HTTPException, status


def add(db: Session, request: ClientBase):
    new_client = Client(
        client_name=request.name,
        email=request.email,
        address=request.address,
        phone_number=request.phone_number
    )

    db.add(new_client)
    db.commit()
    db.close()
    return new_client


def get_all(db: Session):
    return db.query(Client).all()


def get_client(db: Session, id: int):
    return db.query(Client).filter(Client.id == id).first()


def delete_client(db: Session, id: int):
    client = db.query(Client).filter(Client.id == id).first()

    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Client not found')
    else:
        db.delete(client)
        db.commit()
        db.close()

    return 'Client deleted!'
