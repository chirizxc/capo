"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#Signal``."""

from typing import Literal, TypeAlias, cast

"""Signal enum for context graph queries."""
Signal: TypeAlias = Literal[
    "LOGS",
    "METRICS",
    "TRACES",
    "CONFIG",
    "UNKNOWN",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Signal) -> str:
    return value


def deserialize_cbor(data: str) -> Signal:
    return cast(Signal, data)
