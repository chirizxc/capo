"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#SignalType``."""

from typing import Literal, TypeAlias, cast

"""Telemetry signal type that row-scoped access control applies to."""
SignalType: TypeAlias = Literal[
    "LOGS",
    "TRACES",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SignalType) -> str:
    return value


def deserialize_cbor(data: str) -> SignalType:
    return cast(SignalType, data)
