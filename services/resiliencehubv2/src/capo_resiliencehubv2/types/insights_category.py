"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#InsightsCategory``."""

from typing import Literal, TypeAlias, cast

InsightsCategory: TypeAlias = Literal[
    "CROSS_REGION",
    "NEW_DEPENDENCY",
    "THIRD_PARTY",
    "UNEVEN_USAGE",
    "AWS_SERVICE",
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightsCategory) -> str:
    return value


def deserialize_json(data: str) -> InsightsCategory:
    return cast(InsightsCategory, data)
