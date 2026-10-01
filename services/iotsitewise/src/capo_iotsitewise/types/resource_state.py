"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ResourceState``."""

from typing import Literal, TypeAlias, cast

"""<p>The lifecycle state of a resource.</p>"""
ResourceState: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceState) -> str:
    return value


def deserialize_json(data: str) -> ResourceState:
    return cast(ResourceState, data)
