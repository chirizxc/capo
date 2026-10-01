"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfChannelInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafka.types.channel_info

__listOfChannelInfo: TypeAlias = list["capo_kafka.types.channel_info.ChannelInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfChannelInfo) -> list:
    import capo_kafka.types.channel_info

    out: list = []
    for item in value:
        out.append(capo_kafka.types.channel_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfChannelInfo:
    import capo_kafka.types.channel_info

    out: __listOfChannelInfo = []
    for item in data:
        if item is None:
            continue
        out.append(capo_kafka.types.channel_info.deserialize_json(item))
    return out
