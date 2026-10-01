"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Format``."""

from typing import Literal, TypeAlias, cast

Format: TypeAlias = Literal[
    "mp4",
    "quicktime",
    "matroska",
    "webm",
    "mxf",
    "wave",
    "avi",
    "mpegts",
    "mpegps",
    "mp3",
    "flac",
    "asf",
    "ogg",
    "three_gp",
    "three_g2",
    "aac",
    "ac3",
    "eac3",
]


# --- restJson1 ser/de ---
def serialize_json(value: Format) -> str:
    return value


def deserialize_json(data: str) -> Format:
    return cast(Format, data)
