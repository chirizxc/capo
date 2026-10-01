"""Generated from Smithy shape ``com.amazonaws.connect#PreEvaluationFilterOperator``."""

from typing import Literal, TypeAlias, cast

PreEvaluationFilterOperator: TypeAlias = Literal["EQUALS",]


# --- restJson1 ser/de ---
def serialize_json(value: PreEvaluationFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> PreEvaluationFilterOperator:
    return cast(PreEvaluationFilterOperator, data)
