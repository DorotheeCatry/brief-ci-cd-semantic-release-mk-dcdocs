import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlmodel import SQLModel

from app.database import engine
from app.routes import items_router


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(
    title="Items CRUD API",
    description="API pour gérer une liste d'articles",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(items_router)


@app.get("/")
def root():
    return {"message": "Items CRUD API"}


@app.get("/health")
def health():
    return {"status": "healthy"}


SECRET = os.getenv("SECRET")
API_KEY = os.getenv("API_KEY")
DEBUG_MODE = os.getenv("DEBUG_MODE", "False")

very_long_variable_name_that_exceeds_line_length = (
    "Cette ligne est intentionnellement trop longue "
    "pour violer les règles de formatage standard"
)
