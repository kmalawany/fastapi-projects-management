from routers.schemas import ProjectBase, TaskBase, EmployeeBase
from sqlalchemy.orm.session import Session
from database.models import Projects, Tasks, Employee
from fastapi import HTTPException, status


def create_project(client_id: int, db: Session, request: ProjectBase):
    new_project = Projects(
        name=request.name,
        start_date=request.start_date,
        end_date=request.end_date,
        is_active=request.is_active,
        client_id=client_id
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


def get_all_projects(db: Session, skip: int = 0, limit: int = 5):
    return db.query(Projects).offset(skip).limit(limit).all()


def get_one_project(db: Session, id: int):
    project = db.query(Projects).filter(Projects.id == id).first()
    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Project not found')
    else:
        return project


def delete_project(db: Session, id: int):
    project = db.query(Projects).filter(Projects.id == id).first()
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Project not found')
    else:
        db.delete(project)
        db.commit()
        db.close()


def create_project_task(project_id: int, db: Session, request: TaskBase):
    tasks = Tasks(
        name=request.name,
        start_date=request.start_date,
        end_date=request.end_date,
        description=request.description,
        project_id=project_id
    )
    db.add(tasks)
    db.commit()
    db.refresh(tasks)

    return tasks


def get_all_project_task(project_id, db: Session):
    return db.query(Tasks).filter(project_id == project_id).all()




