"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormValidationFindingSeverity``."""

from typing import Literal, TypeAlias, cast

EvaluationFormValidationFindingSeverity: TypeAlias = Literal[
    "WARNING",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormValidationFindingSeverity) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormValidationFindingSeverity:
    return cast(EvaluationFormValidationFindingSeverity, data)
