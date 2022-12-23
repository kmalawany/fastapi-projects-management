from fastapi import APIRouter, Depends
from routers.schemas import ProjectBase, Project, TaskBase, Task
from database.database import get_db
from database import projects_db
from sqlalchemy.orm.session import Session

router = APIRouter(prefix='/projects', tags=['Projects Operations'])


@router.post('/{client_id}', response_model=Project)
def create_project(client_id: int, request: ProjectBase, db: Session = Depends(get_db)):
    return projects_db.create_project(client_id, db, request)


@router.get('/all')
def get_all_projects(db: Session = Depends(get_db)):
    return projects_db.get_all_projects(db)


@router.get('/{id}')
def get_project(id: int, db: Session = Depends(get_db)):
    return projects_db.get_one_project(db, id)


@router.delete('')
def delete_project(id: int, db: Session = Depends(get_db)):
    projects_db.delete_project(db, id)
    return 'Project deleted!'


@router.post('/{project_id}/task', response_model=Task)
def create_task(project_id: int, request: TaskBase, db: Session = Depends(get_db)):
    return projects_db.create_project_task(project_id, db, request)


@router.get('/{project_id}/all-tasks')
def get_all_project_tasks(project_id: int, db: Session = Depends(get_db)):
    return projects_db.get_all_project_task(project_id, db)

