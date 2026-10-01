"""Generated from Smithy shape ``com.amazonaws.kafka#ChannelStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The lifecycle state of a channel.</p>"""
ChannelStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "FAILED",
    "SUSPENDING",
    "SUSPENDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelStatus) -> str:
    return value


def deserialize_json(data: str) -> ChannelStatus:
    return cast(ChannelStatus, data)
