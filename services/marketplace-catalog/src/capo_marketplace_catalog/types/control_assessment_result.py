"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ControlAssessmentResult``."""

from typing import Literal, TypeAlias, cast

ControlAssessmentResult: TypeAlias = Literal[
    "PASS",
    "FAIL",
    "NOT_EXECUTED",
    "EXEMPTION_PASS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlAssessmentResult) -> str:
    return value


def deserialize_json(data: str) -> ControlAssessmentResult:
    return cast(ControlAssessmentResult, data)
