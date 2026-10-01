"""Generated from Smithy shape ``com.amazonaws.geomaps#ColorScheme``."""

from typing import Literal, TypeAlias, cast

ColorScheme: TypeAlias = Literal[
    "Light",
    "Dark",
]


# --- restJson1 ser/de ---
def serialize_json(value: ColorScheme) -> str:
    return value


def deserialize_json(data: str) -> ColorScheme:
    return cast(ColorScheme, data)
