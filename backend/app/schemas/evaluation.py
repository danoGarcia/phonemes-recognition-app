from pydantic import BaseModel


class PhonemeResult(BaseModel):
    phoneme: str
    correct: bool
    hint: str | None


class EvaluationResponse(BaseModel):
    word_id: int
    word_text: str
    results: list[PhonemeResult]
    all_correct: bool
