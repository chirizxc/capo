"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#UpdateAlertOutput``."""

from typing_extensions import TypedDict


class UpdateAlertOutput(TypedDict, closed=True):
    pass


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateAlertOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateAlertOutput:
    out: UpdateAlertOutput = {}  # type: ignore[typeddict-item]
    return out
