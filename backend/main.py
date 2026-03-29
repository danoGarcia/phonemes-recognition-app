from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.dictionary import router as dictionary_router
from app.api.v1.evaluation import get_phoneme_model
from app.api.v1.evaluation import router as evaluation_router
from app.ml.phoneme_model import load_phoneme_model


@asynccontextmanager
async def lifespan(app: FastAPI):
    model = load_phoneme_model()
    app.dependency_overrides[get_phoneme_model] = lambda: model
    yield
    app.dependency_overrides.clear()


app = FastAPI(lifespan=lifespan)

app.include_router(dictionary_router, prefix="/api/v1")
app.include_router(evaluation_router, prefix="/api/v1")


@app.get("/")
async def read_root():
    return {"message": "Hello, world!"}
