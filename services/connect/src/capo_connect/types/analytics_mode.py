"""Generated from Smithy shape ``com.amazonaws.connect#AnalyticsMode``."""

from typing import Literal, TypeAlias, cast

AnalyticsMode: TypeAlias = Literal[
    "PostContact",
    "RealTime",
    "ContactLens",
    "AutomatedInteraction",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsMode) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsMode:
    return cast(AnalyticsMode, data)
