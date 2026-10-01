"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#TranscriptFormat``."""

from typing import Literal, TypeAlias, cast

TranscriptFormat: TypeAlias = Literal[
    "spoken",
    "written",
]


# --- restJson1 ser/de ---
def serialize_json(value: TranscriptFormat) -> str:
    return value


def deserialize_json(data: str) -> TranscriptFormat:
    return cast(TranscriptFormat, data)
