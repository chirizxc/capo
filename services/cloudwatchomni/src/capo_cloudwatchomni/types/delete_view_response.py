"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DeleteViewResponse``."""

from typing_extensions import TypedDict


class DeleteViewResponse(TypedDict, closed=True):
    pass


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteViewResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteViewResponse:
    out: DeleteViewResponse = {}  # type: ignore[typeddict-item]
    return out
