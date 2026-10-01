"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#BusState``."""

from typing import Literal, TypeAlias, cast

"""Lifecycle state of an event bus. - CREATING: Bus creation is in progress. - CREATE_FAILED: Bus creation failed; see StateReason. The bus cannot be recovered or recreated in place: delete it with DeleteEventBus, then create a new bus. - ACTIVE: Bus is fully operational and can accept events. - UPDATING: Bus update is in progress. - UPDATE_FAILED: Bus update failed; the bus remains operational with its previous configuration. - DELETING: Bus deletion is actively in progress. - DELETE_FAILED: Bus deletion failed; see StateReason. Retry DeleteEventBus after removing subscribers and event sources."""
BusState: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "UPDATING",
    "UPDATE_FAILED",
    "DELETING",
    "ACTIVE",
    "DELETE_FAILED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BusState) -> str:
    return value


def deserialize_cbor(data: str) -> BusState:
    return cast(BusState, data)
