"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormMetricType``."""

from typing import Literal, TypeAlias, cast

EvaluationFormMetricType: TypeAlias = Literal["BUSINESS_OUTCOME",]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormMetricType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormMetricType:
    return cast(EvaluationFormMetricType, data)
