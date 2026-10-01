"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmfcScte35Source``."""

from typing import Literal, TypeAlias, cast

"""Ignore this setting unless you have SCTE-35 markers in your input video file. Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want those SCTE-35 markers in this output. When your input is an HLS manifest, choose Manifest cues to pass through CUE markers in your HLS manifest as segment boundaries and SCTE-35 markers in this output at each EXT-X-CUE-OUT splice point in the input manifest."""
CmfcScte35Source: TypeAlias = Literal[
    "PASSTHROUGH",
    "NONE",
    "MANIFEST_CUES",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmfcScte35Source) -> str:
    return value


def deserialize_json(data: str) -> CmfcScte35Source:
    return cast(CmfcScte35Source, data)
