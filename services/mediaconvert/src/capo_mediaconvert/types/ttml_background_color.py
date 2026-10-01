"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TtmlBackgroundColor``."""

from typing import Literal, TypeAlias, cast

"""Specify the background color for TTML captions output."""
TtmlBackgroundColor: TypeAlias = Literal[
    "NONE",
    "BLACK",
    "WHITE",
    "AUTO",
]


# --- restJson1 ser/de ---
def serialize_json(value: TtmlBackgroundColor) -> str:
    return value


def deserialize_json(data: str) -> TtmlBackgroundColor:
    return cast(TtmlBackgroundColor, data)
