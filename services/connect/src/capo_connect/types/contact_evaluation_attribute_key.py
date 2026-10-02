"""Generated from Smithy shape ``com.amazonaws.connect#ContactEvaluationAttributeKey``."""

from typing import Literal, TypeAlias, cast

ContactEvaluationAttributeKey: TypeAlias = Literal["ContactAgentId",]


# --- restJson1 ser/de ---
def serialize_json(value: ContactEvaluationAttributeKey) -> str:
    return value


def deserialize_json(data: str) -> ContactEvaluationAttributeKey:
    return cast(ContactEvaluationAttributeKey, data)
