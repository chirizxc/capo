"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#EdgeType``."""

from typing import Literal, TypeAlias, cast

"""Context graph edge types."""
EdgeType: TypeAlias = Literal[
    "CALLS",
    "ACCESSES",
    "RUNS_ON",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EdgeType) -> str:
    return value


def deserialize_cbor(data: str) -> EdgeType:
    return cast(EdgeType, data)
