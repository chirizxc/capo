"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormValidationStatus``."""

from typing import Literal, TypeAlias, cast

EvaluationFormValidationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormValidationStatus) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormValidationStatus:
    return cast(EvaluationFormValidationStatus, data)
