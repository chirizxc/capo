"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#TagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridgev2.types.tag_key

TagKeyList: TypeAlias = list["capo_eventbridgev2.types.tag_key.TagKey"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagKeyList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> TagKeyList:
    return [item for item in data if item is not None]
