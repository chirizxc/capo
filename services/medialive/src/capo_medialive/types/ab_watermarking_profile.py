"""Generated from Smithy shape ``com.amazonaws.medialive#AbWatermarkingProfile``."""

from typing import Literal, TypeAlias, cast

"""Ab Watermarking Profile"""
AbWatermarkingProfile: TypeAlias = Literal[
    "CAMCORDING",
    "CUSTOM",
    "DEFAULT",
    "HQ",
    "MEZZANINE",
    "ROBUST",
]


# --- restJson1 ser/de ---
def serialize_json(value: AbWatermarkingProfile) -> str:
    return value


def deserialize_json(data: str) -> AbWatermarkingProfile:
    return cast(AbWatermarkingProfile, data)
