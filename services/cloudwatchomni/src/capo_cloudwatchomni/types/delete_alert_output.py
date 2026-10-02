"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DeleteAlertOutput``."""

from typing_extensions import TypedDict


class DeleteAlertOutput(TypedDict, closed=True):
    pass


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteAlertOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteAlertOutput:
    out: DeleteAlertOutput = {}  # type: ignore[typeddict-item]
    return out
