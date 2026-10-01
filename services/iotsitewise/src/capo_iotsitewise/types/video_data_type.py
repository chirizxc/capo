"""Generated from Smithy shape ``com.amazonaws.iotsitewise#VideoDataType``."""

from typing import Literal, TypeAlias, cast

"""<p>The allowed video data types.</p>"""
VideoDataType: TypeAlias = Literal["VIDEO-MP4",]


# --- restJson1 ser/de ---
def serialize_json(value: VideoDataType) -> str:
    return value


def deserialize_json(data: str) -> VideoDataType:
    return cast(VideoDataType, data)
