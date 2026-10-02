"""Generated from Smithy shape ``com.amazonaws.artifact#FeedbackRating``."""

from typing import Literal, TypeAlias, cast

FeedbackRating: TypeAlias = Literal[
    "THUMBS_UP",
    "THUMBS_DOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: FeedbackRating) -> str:
    return value


def deserialize_json(data: str) -> FeedbackRating:
    return cast(FeedbackRating, data)
