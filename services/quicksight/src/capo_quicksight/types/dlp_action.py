"""Generated from Smithy shape ``com.amazonaws.quicksight#DlpAction``."""

from typing import Literal, TypeAlias, cast

DlpAction: TypeAlias = Literal[
    "ALLOW",
    "WARN",
    "BLOCK",
]


# --- restJson1 ser/de ---
def serialize_json(value: DlpAction) -> str:
    return value


def deserialize_json(data: str) -> DlpAction:
    return cast(DlpAction, data)
