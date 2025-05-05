from fastapi import FastAPI
from app.routes import enderecos
from app import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(enderecos.router)
