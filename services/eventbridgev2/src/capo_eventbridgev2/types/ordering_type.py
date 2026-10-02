"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#OrderingType``."""

from typing import Literal, TypeAlias, cast

"""Delivery ordering mode of a subscriber: FIFO delivers events in order within an event group; UNORDERED delivers without an ordering guarantee."""
OrderingType: TypeAlias = Literal[
    "FIFO",
    "UNORDERED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrderingType) -> str:
    return value


def deserialize_cbor(data: str) -> OrderingType:
    return cast(OrderingType, data)
