"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AacPassthroughControl``."""

from typing import Literal, TypeAlias, cast

"""When set to WHEN_POSSIBLE, input AAC audio will be passed through if it is present on the input. This detection is dynamic over the life of the transcode. Inputs that alternate between AAC and non-AAC content will have a consistent AAC output as the system alternates between passthrough and encoding."""
AacPassthroughControl: TypeAlias = Literal[
    "WHEN_POSSIBLE",
    "NO_PASSTHROUGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: AacPassthroughControl) -> str:
    return value


def deserialize_json(data: str) -> AacPassthroughControl:
    return cast(AacPassthroughControl, data)
