"""Generated from Smithy shape ``com.amazonaws.connect#ContactEvaluationAttributeComparisonType``."""

from typing import Literal, TypeAlias, cast

ContactEvaluationAttributeComparisonType: TypeAlias = Literal["EXACT",]


# --- restJson1 ser/de ---
def serialize_json(value: ContactEvaluationAttributeComparisonType) -> str:
    return value


def deserialize_json(data: str) -> ContactEvaluationAttributeComparisonType:
    return cast(ContactEvaluationAttributeComparisonType, data)
