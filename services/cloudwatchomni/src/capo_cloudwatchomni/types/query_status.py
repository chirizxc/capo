"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#QueryStatus``."""

from typing import Literal, TypeAlias, cast

"""The current status of a telemetry query."""
QueryStatus: TypeAlias = Literal[
    "Running",
    "Failed",
    "Complete",
    "Cancelled",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: QueryStatus) -> str:
    return value


def deserialize_cbor(data: str) -> QueryStatus:
    return cast(QueryStatus, data)
