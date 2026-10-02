"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Hdr10PlusPresence``."""

from typing import Literal, TypeAlias, cast

"""Indicates that HDR10+ (SMPTE ST 2094-40) dynamic metadata was detected in the HEVC bitstream. Present only when detected."""
Hdr10PlusPresence: TypeAlias = Literal["PRESENT",]


# --- restJson1 ser/de ---
def serialize_json(value: Hdr10PlusPresence) -> str:
    return value


def deserialize_json(data: str) -> Hdr10PlusPresence:
    return cast(Hdr10PlusPresence, data)
