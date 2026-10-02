"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DiversityCapType``."""

from typing import Literal, TypeAlias, cast

DiversityCapType: TypeAlias = Literal[
    "PERCENTAGE",
    "VALUE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DiversityCapType) -> str:
    return value


def deserialize_json(data: str) -> DiversityCapType:
    return cast(DiversityCapType, data)
