"""Generated from Smithy shape ``com.amazonaws.mediatailor#PreRollAdSequencingMode``."""

from typing import Literal, TypeAlias, cast

PreRollAdSequencingMode: TypeAlias = Literal[
    "FOLLOW_AD_SEQUENCE",
    "IGNORE_AD_SEQUENCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: PreRollAdSequencingMode) -> str:
    return value


def deserialize_json(data: str) -> PreRollAdSequencingMode:
    return cast(PreRollAdSequencingMode, data)
