"""Generated from Smithy shape ``com.amazonaws.guardduty#AssociationMode``."""

from typing import Literal, TypeAlias, cast

AssociationMode: TypeAlias = Literal[
    "LIVE",
    "DRY_RUN",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociationMode) -> str:
    return value


def deserialize_json(data: str) -> AssociationMode:
    return cast(AssociationMode, data)
