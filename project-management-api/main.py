from fastapi import FastAPI
from database import models
from database.database import engine
from routers import projects, clients, employees

models.Base.metadata.create_all(engine)
app = FastAPI()
app.include_router(projects.router)
app.include_router(clients.router)
app.include_router(employees.router)


@app.get('/')
def hello_world():
    return {'message': 'Hello world'}
