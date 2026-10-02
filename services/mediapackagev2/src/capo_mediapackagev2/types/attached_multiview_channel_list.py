"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#AttachedMultiviewChannelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.resource_name

AttachedMultiviewChannelList: TypeAlias = list[
    "capo_mediapackagev2.types.resource_name.ResourceName"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttachedMultiviewChannelList) -> list:
    return list(value)


def deserialize_json(data: list) -> AttachedMultiviewChannelList:
    return [item for item in data if item is not None]
