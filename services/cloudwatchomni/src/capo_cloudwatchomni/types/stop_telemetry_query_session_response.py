"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#StopTelemetryQuerySessionResponse``."""

from typing_extensions import TypedDict


class StopTelemetryQuerySessionResponse(TypedDict, closed=True):
    pass


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StopTelemetryQuerySessionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> StopTelemetryQuerySessionResponse:
    out: StopTelemetryQuerySessionResponse = {}  # type: ignore[typeddict-item]
    return out
