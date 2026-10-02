"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TtmlFontStyle``."""

from typing import Literal, TypeAlias, cast

"""Specify the font style for TTML captions output."""
TtmlFontStyle: TypeAlias = Literal[
    "NORMAL",
    "ITALIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: TtmlFontStyle) -> str:
    return value


def deserialize_json(data: str) -> TtmlFontStyle:
    return cast(TtmlFontStyle, data)
