## Phase 1: Test Suite (TDD)
**Goal:** Write all failing tests that define the evaluation contract. No implementation code exists yet — every test should fail with `ImportError` or `ModuleNotFoundError` by the end of this phase.

### [Task 1] Add ML dependencies
* **ID:** 1
    - [x] 1.1: Add `transformers (>=4.40.0,<5.0.0)`, `torch (>=2.2.0)`, `torchaudio (>=2.2.0)`, `librosa (>=0.10.0)`, `soundfile (>=0.12.0)` to `backend/pyproject.toml` under `[project] dependencies`.

### [Task 2] Evaluation Service tests
* **ID:** 2
    - [x] 2.1: Create `backend/tests/test_evaluation_service.py`. Write a test for `evaluate_pronunciation()` with an exact-match model output → asserts `all_correct=True` and all hints `None`.
    - [x] 2.2: Write a test for a substitution error (model returns `["f", "ɪ", "ŋ", "k"]` for "think") → asserts first phoneme is wrong and hint is populated from `ERROR_MAP`.
    - [x] 2.3: Write a test for a deletion error (model returns fewer phonemes than target) → asserts missing positions are `correct=False` with `hint=None`.
    - [x] 2.4: Write a test for extra phonemes (insertions) → asserts `results` length equals the target word's IPA length (insertions are ignored).
    - [x] 2.5: Write a test that calls `evaluate_pronunciation()` with a non-existent `word_id` → asserts `HTTPException(404)`.
    - [x] 2.6: Write a test where `model.predict()` raises an exception → asserts `HTTPException(422)`.
    - [x] 2.7: Write a test for a substitution not present in `ERROR_MAP` → asserts `correct=False` and `hint=None` (no `KeyError`).

### [Task 3] Evaluation Router tests
* **ID:** 3
    - [x] 3.1: Create `backend/tests/test_evaluation_router.py`. Wire an `eval_async_client` fixture that overrides both `get_session` and `get_phoneme_model`. Write a test for `POST /api/v1/evaluate` with a valid multipart request (`.wav` bytes + `word_id` form field) → asserts `200` and correct JSON schema (`word_id`, `word_text`, `results`, `all_correct`).
    - [x] 3.2: Write a test with a missing `word_id` form field → asserts `422` (FastAPI validation error).
    - [x] 3.3: Write a test with a non-existent `word_id` → asserts `404`.
    - [x] 3.4: Write a test where `model.predict()` raises → asserts `422`.

---

## Phase 2: Implementation
**Goal:** Write the minimum production code to turn every red test green.

### [Task 4] ML package
* **ID:** 4 | **Dependencies:** 1
    - [x] 4.1: Create `backend/app/ml/__init__.py` (empty package marker).
    - [x] 4.2: Create `backend/app/ml/error_map.py` with a module-level `ERROR_MAP: dict[str, str]`. Key format: `"{target}_{user_produced}"`. Populate 20 entries covering the most common English phoneme substitutions (dental fricatives, vowels, liquids, nasals, sibilants).
    - [x] 4.3: Create `backend/app/ml/phoneme_model.py`. Implement `PhonemeModel` class that loads `facebook/wav2vec2-lv-60-espeak-cv-ft` via `Wav2Vec2Processor` + `Wav2Vec2ForCTC`. `predict(audio_bytes: bytes) -> list[str]` must: load audio with `librosa`, resample to 16 kHz, run `torch.no_grad()` forward pass, decode via `batch_decode`, and return whitespace-split IPA tokens. Expose a `load_phoneme_model()` factory function.

### [Task 5] Evaluation schemas
* **ID:** 5 | **Dependencies:** 4
    - [x] 5.1: Create `backend/app/schemas/evaluation.py`. Define `PhonemeResult(phoneme, correct, hint: str | None)` and `EvaluationResponse(word_id, word_text, results: list[PhonemeResult], all_correct)`.

### [Task 6] Evaluation service
* **ID:** 6 | **Dependencies:** 4, 5
    - [x] 6.1: Create `backend/app/services/evaluation_service.py`. Implement `evaluate_pronunciation(audio_bytes, word_id, db, model)`:
        1. Fetch target word via `get_word_by_id()` (raises 404 if missing).
        2. Call `model.predict()` wrapped in `try/except Exception → HTTP 422`.
        3. Align index-by-index over target phonemes (dictionary is authoritative length). Extra user phonemes beyond target length are ignored. Missing user phonemes (deletions) are `correct=False, hint=None`.
        4. Hint is `ERROR_MAP.get(f"{target}_{produced}")` — `None` on miss, no exception.
    - [x] 6.2: Run `make test` — `test_evaluation_service.py` must be green.

### [Task 7] Evaluation router
* **ID:** 7 | **Dependencies:** 5, 6
    - [x] 7.1: Create `backend/app/api/v1/evaluation.py`. Define `POST /evaluate` route accepting `audio: UploadFile` and `word_id: int = Form(...)`. Expose `get_phoneme_model()` as a dependency injection point (raises `RuntimeError` when called before lifespan override).
    - [x] 7.2: Update `backend/main.py` with a lifespan context manager that calls `load_phoneme_model()` at startup and registers `app.dependency_overrides[get_phoneme_model] = lambda: model`. Register the evaluation router at `/api/v1`.
    - [ ] 7.3: Run `make test` — full suite must be green with no regressions.
