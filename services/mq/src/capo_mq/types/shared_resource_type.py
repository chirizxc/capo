"""Generated from Smithy shape ``com.amazonaws.mq#SharedResourceType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of shared resource.</p>"""
SharedResourceType: TypeAlias = Literal[
    "RESOURCE_SHARE",
    "RESOURCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SharedResourceType) -> str:
    return value


def deserialize_json(data: str) -> SharedResourceType:
    return cast(SharedResourceType, data)
