"""Generated from Smithy shape ``com.amazonaws.geomaps#LabelSize``."""

from typing import Literal, TypeAlias, cast

LabelSize: TypeAlias = Literal[
    "Small",
    "Large",
]


# --- restJson1 ser/de ---
def serialize_json(value: LabelSize) -> str:
    return value


def deserialize_json(data: str) -> LabelSize:
    return cast(LabelSize, data)
