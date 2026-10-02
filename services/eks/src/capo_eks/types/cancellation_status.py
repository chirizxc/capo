"""Generated from Smithy shape ``com.amazonaws.eks#CancellationStatus``."""

from typing import Literal, TypeAlias, cast

CancellationStatus: TypeAlias = Literal[
    "InProgress",
    "Failed",
    "Successful",
]


# --- restJson1 ser/de ---
def serialize_json(value: CancellationStatus) -> str:
    return value


def deserialize_json(data: str) -> CancellationStatus:
    return cast(CancellationStatus, data)
