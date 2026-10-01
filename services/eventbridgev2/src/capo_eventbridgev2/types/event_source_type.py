"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#EventSourceType``."""

from typing import Literal, TypeAlias, cast

"""Origin type of an EventSource: an AWS service's events (AWS_SERVICE_EVENTS) or a partner event source's events (PARTNER_EVENTS)."""
EventSourceType: TypeAlias = Literal[
    "AWS_SERVICE_EVENTS",
    "PARTNER_EVENTS",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventSourceType) -> str:
    return value


def deserialize_cbor(data: str) -> EventSourceType:
    return cast(EventSourceType, data)
