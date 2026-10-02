"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ContentKeyPeriodTiming``."""

from typing import Literal, TypeAlias, cast

ContentKeyPeriodTiming: TypeAlias = Literal[
    "INDEX_ONLY",
    "START_END_ONLY",
    "INDEX_WITH_START_END",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentKeyPeriodTiming) -> str:
    return value


def deserialize_json(data: str) -> ContentKeyPeriodTiming:
    return cast(ContentKeyPeriodTiming, data)
