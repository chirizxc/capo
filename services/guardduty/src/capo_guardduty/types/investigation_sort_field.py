"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationSortField``."""

from typing import Literal, TypeAlias, cast

InvestigationSortField: TypeAlias = Literal[
    "START_TIME",
    "END_TIME",
    "STATUS",
    "RISK_LEVEL",
    "CONFIDENCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationSortField) -> str:
    return value


def deserialize_json(data: str) -> InvestigationSortField:
    return cast(InvestigationSortField, data)
