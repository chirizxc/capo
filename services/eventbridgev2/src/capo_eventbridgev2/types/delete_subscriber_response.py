"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#DeleteSubscriberResponse``."""

from typing_extensions import TypedDict


class DeleteSubscriberResponse(TypedDict, closed=True):
    pass


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteSubscriberResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteSubscriberResponse:
    out: DeleteSubscriberResponse = {}  # type: ignore[typeddict-item]
    return out
