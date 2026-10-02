"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormAIVersionStatus``."""

from typing import Literal, TypeAlias, cast

EvaluationFormAIVersionStatus: TypeAlias = Literal[
    "LATEST",
    "PREVIEW",
    "ACTIVE",
    "DEPRECATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormAIVersionStatus) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormAIVersionStatus:
    return cast(EvaluationFormAIVersionStatus, data)
