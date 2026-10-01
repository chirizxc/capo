"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TtmlFontWeight``."""

from typing import Literal, TypeAlias, cast

"""Specify the font weight for TTML captions output."""
TtmlFontWeight: TypeAlias = Literal[
    "NORMAL",
    "BOLD",
]


# --- restJson1 ser/de ---
def serialize_json(value: TtmlFontWeight) -> str:
    return value


def deserialize_json(data: str) -> TtmlFontWeight:
    return cast(TtmlFontWeight, data)
