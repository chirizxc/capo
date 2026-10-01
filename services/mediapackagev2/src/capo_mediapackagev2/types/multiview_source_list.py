"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#MultiviewSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.resource_name

MultiviewSourceList: TypeAlias = list[
    "capo_mediapackagev2.types.resource_name.ResourceName"
]


# --- restJson1 ser/de ---
def serialize_json(value: MultiviewSourceList) -> list:
    return list(value)


def deserialize_json(data: list) -> MultiviewSourceList:
    return [item for item in data if item is not None]
