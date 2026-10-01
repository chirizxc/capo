"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DisallowIntermediateTableOutput``."""

from typing_extensions import TypedDict


class DisallowIntermediateTableOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DisallowIntermediateTableOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisallowIntermediateTableOutput:
    out: DisallowIntermediateTableOutput = {}  # type: ignore[typeddict-item]
    return out
