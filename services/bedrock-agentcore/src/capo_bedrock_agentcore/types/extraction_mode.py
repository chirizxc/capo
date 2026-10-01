"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ExtractionMode``."""

from typing import Literal, TypeAlias, cast

ExtractionMode: TypeAlias = Literal["SKIP",]


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionMode) -> str:
    return value


def deserialize_json(data: str) -> ExtractionMode:
    return cast(ExtractionMode, data)
