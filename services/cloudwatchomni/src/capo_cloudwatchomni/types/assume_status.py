"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AssumeStatus``."""

from typing import Literal, TypeAlias, cast

"""The calling principal's authorization to assume an access profile."""
AssumeStatus: TypeAlias = Literal[
    "ALLOWED",
    "DENIED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssumeStatus) -> str:
    return value


def deserialize_cbor(data: str) -> AssumeStatus:
    return cast(AssumeStatus, data)
