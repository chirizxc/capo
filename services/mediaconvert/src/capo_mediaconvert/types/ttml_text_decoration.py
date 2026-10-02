"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TtmlTextDecoration``."""

from typing import Literal, TypeAlias, cast

"""Specify the text decoration for TTML captions output."""
TtmlTextDecoration: TypeAlias = Literal[
    "NONE",
    "UNDERLINE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TtmlTextDecoration) -> str:
    return value


def deserialize_json(data: str) -> TtmlTextDecoration:
    return cast(TtmlTextDecoration, data)
