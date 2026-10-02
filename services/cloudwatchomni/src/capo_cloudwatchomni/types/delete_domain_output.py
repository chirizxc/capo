"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DeleteDomainOutput``."""

from typing_extensions import TypedDict


class DeleteDomainOutput(TypedDict, closed=True):
    pass


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteDomainOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteDomainOutput:
    out: DeleteDomainOutput = {}  # type: ignore[typeddict-item]
    return out
