"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DependencyInsightsErrorCode``."""

from typing import Literal, TypeAlias, cast

DependencyInsightsErrorCode: TypeAlias = Literal[
    "INSUFFICIENT_DATA",
    "LLM_GENERATION_FAILED",
    "INTERNAL_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: DependencyInsightsErrorCode) -> str:
    return value


def deserialize_json(data: str) -> DependencyInsightsErrorCode:
    return cast(DependencyInsightsErrorCode, data)
