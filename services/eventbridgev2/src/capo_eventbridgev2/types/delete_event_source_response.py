"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#DeleteEventSourceResponse``."""

from typing_extensions import TypedDict


class DeleteEventSourceResponse(TypedDict, closed=True):
    pass


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteEventSourceResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteEventSourceResponse:
    out: DeleteEventSourceResponse = {}  # type: ignore[typeddict-item]
    return out
