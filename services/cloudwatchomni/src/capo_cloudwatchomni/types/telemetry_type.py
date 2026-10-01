"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#TelemetryType``."""

from typing import Literal, TypeAlias, cast

"""The type of telemetry data."""
TelemetryType: TypeAlias = Literal[
    "LOGS",
    "TRACES",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TelemetryType) -> str:
    return value


def deserialize_cbor(data: str) -> TelemetryType:
    return cast(TelemetryType, data)
