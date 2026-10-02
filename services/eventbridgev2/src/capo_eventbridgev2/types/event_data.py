"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#EventData``."""

from typing import TypeAlias

"""The event data of a raw publish entry, as a base64-encoded blob."""
EventData: TypeAlias = bytes


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventData) -> EventData:
    return value


def deserialize_cbor(data: EventData) -> EventData:
    return data
