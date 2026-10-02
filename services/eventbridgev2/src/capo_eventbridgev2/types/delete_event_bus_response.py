"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#DeleteEventBusResponse``."""

from typing_extensions import TypedDict


class DeleteEventBusResponse(TypedDict, closed=True):
    pass


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteEventBusResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteEventBusResponse:
    out: DeleteEventBusResponse = {}  # type: ignore[typeddict-item]
    return out
