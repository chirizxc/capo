"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#EventSourceState``."""

from typing import Literal, TypeAlias, cast

"""Lifecycle state of an EventSource. Revocation is reported by the Revoked flag."""
EventSourceState: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "CREATE_FAILED",
    "UPDATE_FAILED",
    "DELETING",
    "DELETE_FAILED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventSourceState) -> str:
    return value


def deserialize_cbor(data: str) -> EventSourceState:
    return cast(EventSourceState, data)
