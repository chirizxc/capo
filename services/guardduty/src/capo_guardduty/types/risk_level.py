"""Generated from Smithy shape ``com.amazonaws.guardduty#RiskLevel``."""

from typing import Literal, TypeAlias, cast

RiskLevel: TypeAlias = Literal[
    "Info",
    "Low",
    "Medium",
    "High",
    "Critical",
]


# --- restJson1 ser/de ---
def serialize_json(value: RiskLevel) -> str:
    return value


def deserialize_json(data: str) -> RiskLevel:
    return cast(RiskLevel, data)
