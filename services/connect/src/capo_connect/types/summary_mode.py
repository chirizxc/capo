"""Generated from Smithy shape ``com.amazonaws.connect#SummaryMode``."""

from typing import Literal, TypeAlias, cast

SummaryMode: TypeAlias = Literal[
    "PostContact",
    "AutomatedInteraction",
    "ContactChain",
]


# --- restJson1 ser/de ---
def serialize_json(value: SummaryMode) -> str:
    return value


def deserialize_json(data: str) -> SummaryMode:
    return cast(SummaryMode, data)
