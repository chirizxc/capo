"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfMotionImageInserter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.motion_image_inserter

__listOfMotionImageInserter: TypeAlias = list[
    "capo_mediaconvert.types.motion_image_inserter.MotionImageInserter"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMotionImageInserter) -> list:
    import capo_mediaconvert.types.motion_image_inserter

    out: list = []
    for item in value:
        out.append(capo_mediaconvert.types.motion_image_inserter.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfMotionImageInserter:
    import capo_mediaconvert.types.motion_image_inserter

    out: __listOfMotionImageInserter = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mediaconvert.types.motion_image_inserter.deserialize_json(item))
    return out
