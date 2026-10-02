"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationStatus``."""

from typing import Literal, TypeAlias, cast

InvestigationStatus: TypeAlias = Literal[
    "RUNNING",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationStatus) -> str:
    return value


def deserialize_json(data: str) -> InvestigationStatus:
    return cast(InvestigationStatus, data)
