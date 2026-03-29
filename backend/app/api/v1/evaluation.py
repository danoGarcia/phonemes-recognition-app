from typing import Annotated

from fastapi import APIRouter, Depends, Form, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.ml.phoneme_model import PhonemeModel
from app.schemas.evaluation import EvaluationResponse
from app.services.evaluation_service import evaluate_pronunciation

router = APIRouter(prefix="/evaluate", tags=["evaluation"])

DbSession = Annotated[AsyncSession, Depends(get_session)]


def get_phoneme_model() -> PhonemeModel:
    raise RuntimeError("PhonemeModel not initialized — lifespan did not run")


PhonemeModelDep = Annotated[PhonemeModel, Depends(get_phoneme_model)]


@router.post("", response_model=EvaluationResponse)
async def evaluate_word(
    audio: UploadFile,
    word_id: int = Form(...),
    lang: str = Form("es"),
    db: DbSession = None,
    model: PhonemeModelDep = None,
) -> EvaluationResponse:
    audio_bytes = await audio.read()
    return await evaluate_pronunciation(
        audio_bytes=audio_bytes,
        word_id=word_id,
        db=db,
        model=model,
        lang=lang,
    )
