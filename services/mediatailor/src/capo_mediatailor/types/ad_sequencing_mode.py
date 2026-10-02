"""Generated from Smithy shape ``com.amazonaws.mediatailor#AdSequencingMode``."""

from typing import Literal, TypeAlias, cast

AdSequencingMode: TypeAlias = Literal[
    "FOLLOW_AD_SEQUENCE",
    "IGNORE_AD_SEQUENCE",
    "FOLLOW_AD_SEQUENCE_ONLY_LIVE",
    "FOLLOW_AD_SEQUENCE_ONLY_VOD",
]


# --- restJson1 ser/de ---
def serialize_json(value: AdSequencingMode) -> str:
    return value


def deserialize_json(data: str) -> AdSequencingMode:
    return cast(AdSequencingMode, data)
