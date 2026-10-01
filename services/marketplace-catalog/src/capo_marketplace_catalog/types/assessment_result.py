"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#AssessmentResult``."""

from typing import Literal, TypeAlias, cast

AssessmentResult: TypeAlias = Literal[
    "PASS",
    "FAIL",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentResult) -> str:
    return value


def deserialize_json(data: str) -> AssessmentResult:
    return cast(AssessmentResult, data)
