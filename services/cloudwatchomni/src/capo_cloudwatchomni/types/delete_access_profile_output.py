"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DeleteAccessProfileOutput``."""

from typing_extensions import TypedDict


class DeleteAccessProfileOutput(TypedDict, closed=True):
    pass


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteAccessProfileOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteAccessProfileOutput:
    out: DeleteAccessProfileOutput = {}  # type: ignore[typeddict-item]
    return out
