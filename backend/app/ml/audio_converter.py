from __future__ import annotations

import io

from pydub import AudioSegment


class AudioConversionError(Exception):
    """Raised when audio conversion to WAV fails."""


def convert_audio_to_wav(audio_bytes: bytes) -> bytes:
    """Convert audio bytes in any format (webm, mp3, ogg, etc.) to WAV.

    Uses pydub + ffmpeg under the hood.

    Raises:
        AudioConversionError: If the conversion fails for any reason.
    """
    try:
        segment = AudioSegment.from_file(io.BytesIO(audio_bytes))
        buffer = io.BytesIO()
        segment.export(buffer, format="wav")
        return buffer.getvalue()
    except Exception as exc:
        raise AudioConversionError(str(exc)) from exc
