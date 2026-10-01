"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#StopTelemetryQueryResponse``."""

from typing_extensions import TypedDict


class StopTelemetryQueryResponse(TypedDict, closed=True):
    pass


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StopTelemetryQueryResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> StopTelemetryQueryResponse:
    out: StopTelemetryQueryResponse = {}  # type: ignore[typeddict-item]
    return out
