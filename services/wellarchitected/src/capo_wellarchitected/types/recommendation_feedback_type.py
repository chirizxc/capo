"""Generated from Smithy shape ``com.amazonaws.wellarchitected#RecommendationFeedbackType``."""

from typing import Literal, TypeAlias, cast

RecommendationFeedbackType: TypeAlias = Literal[
    "USEFUL",
    "NOT_USEFUL",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationFeedbackType) -> str:
    return value


def deserialize_json(data: str) -> RecommendationFeedbackType:
    return cast(RecommendationFeedbackType, data)
