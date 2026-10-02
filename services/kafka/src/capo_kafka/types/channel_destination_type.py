"""Generated from Smithy shape ``com.amazonaws.kafka#ChannelDestinationType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of destination configured for the channel.</p>"""
ChannelDestinationType: TypeAlias = Literal[
    "ICEBERG",
    "S3",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelDestinationType) -> str:
    return value


def deserialize_json(data: str) -> ChannelDestinationType:
    return cast(ChannelDestinationType, data)
