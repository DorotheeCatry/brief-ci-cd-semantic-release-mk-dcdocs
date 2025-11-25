import os
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI
from sqlmodel import SQLModel

from app.database import engine
from app.routes import items_router


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI) -> AsyncGenerator[Any, None]:
    SQLModel.metadata.create_all(engine)
    yield


version = "0.1.0"

app = FastAPI(
    title="Items API",
    description="API de gestion d'items avec CI/CD",
    version=version,
    lifespan=lifespan,
)

app.include_router(items_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Items CRUD API"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy"}


SECRET = os.getenv("SECRET")
API_KEY = os.getenv("API_KEY")
DEBUG_MODE = os.getenv("DEBUG_MODE", "False")

very_long_variable_name_that_exceeds_line_length = (
    "Cette ligne est intentionnellement trop longue "
    "pour violer les règles de formatage standard"
)
