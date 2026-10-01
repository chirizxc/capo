"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DeleteIntegrationOutput``."""

from typing_extensions import TypedDict


class DeleteIntegrationOutput(TypedDict, closed=True):
    pass


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteIntegrationOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteIntegrationOutput:
    out: DeleteIntegrationOutput = {}  # type: ignore[typeddict-item]
    return out
