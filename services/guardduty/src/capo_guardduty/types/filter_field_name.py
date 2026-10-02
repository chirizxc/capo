"""Generated from Smithy shape ``com.amazonaws.guardduty#FilterFieldName``."""

from typing import Literal, TypeAlias, cast

FilterFieldName: TypeAlias = Literal[
    "name",
    "description",
    "dataSource",
    "severity",
    "tactic",
    "technique",
    "service",
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterFieldName) -> str:
    return value


def deserialize_json(data: str) -> FilterFieldName:
    return cast(FilterFieldName, data)
