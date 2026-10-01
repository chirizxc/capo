"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DeleteSpaceOutput``."""

from typing_extensions import TypedDict


class DeleteSpaceOutput(TypedDict, closed=True):
    pass


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteSpaceOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteSpaceOutput:
    out: DeleteSpaceOutput = {}  # type: ignore[typeddict-item]
    return out
