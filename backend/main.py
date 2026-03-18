from database.db import Base, engine
from core import models

Base.metadata.create_all(bind=engine)

from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="ChronoFuture OS v3.0",
    description="Civilización Ciber Maya",
    version="3.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {
        "system": "ChronoFuture OS",
        "status": "online",
        "message": "Núcleo ciber maya iniciado"
    }
