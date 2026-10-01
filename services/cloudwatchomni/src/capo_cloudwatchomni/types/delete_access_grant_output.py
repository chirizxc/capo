"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DeleteAccessGrantOutput``."""

from typing_extensions import TypedDict


class DeleteAccessGrantOutput(TypedDict, closed=True):
    pass


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteAccessGrantOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteAccessGrantOutput:
    out: DeleteAccessGrantOutput = {}  # type: ignore[typeddict-item]
    return out
