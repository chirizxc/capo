"""Generated from Smithy shape ``com.amazonaws.connect#PreEvaluationFilterType``."""

from typing import Literal, TypeAlias, cast

PreEvaluationFilterType: TypeAlias = Literal["TAG",]


# --- restJson1 ser/de ---
def serialize_json(value: PreEvaluationFilterType) -> str:
    return value


def deserialize_json(data: str) -> PreEvaluationFilterType:
    return cast(PreEvaluationFilterType, data)
