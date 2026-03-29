import pytest
import pytest_asyncio
from unittest.mock import MagicMock
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.word import Word
from app.core.database import get_session
from app.api.v1.evaluation import get_phoneme_model
from main import app


@pytest.fixture
def mock_model():
    model = MagicMock()
    model.predict.return_value = ["θ", "ɪ", "ŋ", "k"]
    return model


@pytest_asyncio.fixture
async def eval_async_client(db_session: AsyncSession, mock_model):
    async def override_get_session():
        yield db_session

    app.dependency_overrides[get_session] = override_get_session
    app.dependency_overrides[get_phoneme_model] = lambda: mock_model

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client

    app.dependency_overrides.clear()


async def test_evaluate_returns_200(
    eval_async_client: AsyncClient, db_session: AsyncSession, mock_model
):
    word = Word(text="Think", ipa=["θ", "ɪ", "ŋ", "k"])
    db_session.add(word)
    await db_session.commit()
    await db_session.refresh(word)

    response = await eval_async_client.post(
        "/api/v1/evaluate",
        data={"word_id": word.id},
        files={"audio": ("test.wav", b"fake_audio", "audio/wav")},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["word_id"] == word.id
    assert data["word_text"] == "Think"
    assert len(data["results"]) == 4
    assert data["all_correct"] is True


async def test_evaluate_missing_word_id(eval_async_client: AsyncClient):
    response = await eval_async_client.post(
        "/api/v1/evaluate",
        files={"audio": ("test.wav", b"fake_audio", "audio/wav")},
    )
    assert response.status_code == 422


async def test_evaluate_word_not_found(eval_async_client: AsyncClient):
    response = await eval_async_client.post(
        "/api/v1/evaluate",
        data={"word_id": 9999},
        files={"audio": ("test.wav", b"fake_audio", "audio/wav")},
    )
    assert response.status_code == 404


async def test_evaluate_bad_audio(
    eval_async_client: AsyncClient, db_session: AsyncSession, mock_model
):
    word = Word(text="Think", ipa=["θ", "ɪ", "ŋ", "k"])
    db_session.add(word)
    await db_session.commit()
    await db_session.refresh(word)

    mock_model.predict.side_effect = ValueError("corrupt")

    response = await eval_async_client.post(
        "/api/v1/evaluate",
        data={"word_id": word.id},
        files={"audio": ("test.wav", b"bad_audio", "audio/wav")},
    )
    assert response.status_code == 422
