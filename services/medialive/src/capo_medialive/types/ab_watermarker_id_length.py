"""Generated from Smithy shape ``com.amazonaws.medialive#AbWatermarkerIdLength``."""

from typing import Literal, TypeAlias, cast

"""Ab Watermarker Id Length"""
AbWatermarkerIdLength: TypeAlias = Literal[
    "ID_2048",
    "ID_512",
]


# --- restJson1 ser/de ---
def serialize_json(value: AbWatermarkerIdLength) -> str:
    return value


def deserialize_json(data: str) -> AbWatermarkerIdLength:
    return cast(AbWatermarkerIdLength, data)
