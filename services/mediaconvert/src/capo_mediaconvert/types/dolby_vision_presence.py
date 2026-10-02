"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DolbyVisionPresence``."""

from typing import Literal, TypeAlias, cast

"""Whether a Dolby Vision component is present in the track."""
DolbyVisionPresence: TypeAlias = Literal[
    "PRESENT",
    "ABSENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: DolbyVisionPresence) -> str:
    return value


def deserialize_json(data: str) -> DolbyVisionPresence:
    return cast(DolbyVisionPresence, data)
