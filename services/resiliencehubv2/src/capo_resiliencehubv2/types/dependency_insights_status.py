"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DependencyInsightsStatus``."""

from typing import Literal, TypeAlias, cast

DependencyInsightsStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DependencyInsightsStatus) -> str:
    return value


def deserialize_json(data: str) -> DependencyInsightsStatus:
    return cast(DependencyInsightsStatus, data)
