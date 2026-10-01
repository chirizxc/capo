"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#EventBusV2MetadataMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridgev2.types.string

EventBusV2MetadataMap: TypeAlias = dict[
    "capo_eventbridgev2.types.string.String", "capo_eventbridgev2.types.string.String"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: EventBusV2MetadataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> EventBusV2MetadataMap:
    out: EventBusV2MetadataMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
