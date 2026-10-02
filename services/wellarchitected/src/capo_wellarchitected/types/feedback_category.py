"""Generated from Smithy shape ``com.amazonaws.wellarchitected#FeedbackCategory``."""

from typing import Literal, TypeAlias, cast

FeedbackCategory: TypeAlias = Literal[
    "OTHER",
    "RECOMMENDATION_NOT_RELEVANT",
    "RESOURCE_NOT_IMPORTANT",
    "RESOURCE_TYPE_NOT_IMPORTANT",
    "RECOMMENDATION_INCORRECT",
]


# --- restJson1 ser/de ---
def serialize_json(value: FeedbackCategory) -> str:
    return value


def deserialize_json(data: str) -> FeedbackCategory:
    return cast(FeedbackCategory, data)
