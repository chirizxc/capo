"""Generated from Smithy shape ``com.amazonaws.quicksight#ApplicableToType``."""

from typing import Literal, TypeAlias, cast

ApplicableToType: TypeAlias = Literal["GROUP",]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicableToType) -> str:
    return value


def deserialize_json(data: str) -> ApplicableToType:
    return cast(ApplicableToType, data)
