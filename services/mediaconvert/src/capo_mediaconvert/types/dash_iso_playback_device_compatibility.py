"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DashIsoPlaybackDeviceCompatibility``."""

from typing import Literal, TypeAlias, cast

"""This setting can improve the compatibility of your output with video players on obsolete devices. It applies only to DASH outputs with DRM encryption. Choose Unencrypted SEI only to correct problems with playback on older H.264 devices. Choose CENC v1 unencrypted headers to leave NAL unit headers and slice headers unencrypted for H.265 outputs, improving compatibility with strict HEVC decoders. Otherwise, keep the default setting CENC v1."""
DashIsoPlaybackDeviceCompatibility: TypeAlias = Literal[
    "CENC_V1",
    "UNENCRYPTED_SEI",
    "CENC_V1_UNENCRYPTED_HEADERS",
]


# --- restJson1 ser/de ---
def serialize_json(value: DashIsoPlaybackDeviceCompatibility) -> str:
    return value


def deserialize_json(data: str) -> DashIsoPlaybackDeviceCompatibility:
    return cast(DashIsoPlaybackDeviceCompatibility, data)
