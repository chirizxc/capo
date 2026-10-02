"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TtmlFontColor``."""

from typing import Literal, TypeAlias, cast

"""Specify the font color for TTML captions output."""
TtmlFontColor: TypeAlias = Literal[
    "WHITE",
    "BLACK",
    "YELLOW",
    "RED",
    "GREEN",
    "BLUE",
    "AUTO",
]


# --- restJson1 ser/de ---
def serialize_json(value: TtmlFontColor) -> str:
    return value


def deserialize_json(data: str) -> TtmlFontColor:
    return cast(TtmlFontColor, data)
