"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#PutEventsResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridgev2.types.event_resource

PutEventsResourceList: TypeAlias = list[
    "capo_eventbridgev2.types.event_resource.EventResource"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutEventsResourceList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> PutEventsResourceList:
    return [item for item in data if item is not None]
