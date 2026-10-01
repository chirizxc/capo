"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioSmpte337Passthrough``."""

from typing import Literal, TypeAlias, cast

"""Specify whether to pass SMPTE 337M-wrapped audio (such as Dolby E) through without unwrapping. Choose Enabled to pass the SMPTE 337M container through unchanged, treating the track as raw PCM. Choose Disabled (default) to automatically detect and unwrap SMPTE 337M data, extracting the underlying Dolby E programs as separate audio tracks for encoding. When this field is absent, the service defaults to Disabled (auto-unwrap)."""
AudioSmpte337Passthrough: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioSmpte337Passthrough) -> str:
    return value


def deserialize_json(data: str) -> AudioSmpte337Passthrough:
    return cast(AudioSmpte337Passthrough, data)
