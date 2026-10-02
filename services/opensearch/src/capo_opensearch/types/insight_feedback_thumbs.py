"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightFeedbackThumbs``."""

from typing import Literal, TypeAlias, cast

"""<p>The thumbs up or thumbs down feedback for an insight. Possible values are <code>Up</code> and <code>Down</code>.</p>"""
InsightFeedbackThumbs: TypeAlias = Literal[
    "Up",
    "Down",
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightFeedbackThumbs) -> str:
    return value


def deserialize_json(data: str) -> InsightFeedbackThumbs:
    return cast(InsightFeedbackThumbs, data)
