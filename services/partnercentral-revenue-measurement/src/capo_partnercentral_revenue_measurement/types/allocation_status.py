"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#AllocationStatus``."""

from typing import Literal, TypeAlias, cast

AllocationStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AllocationStatus) -> str:
    return value


def deserialize_cbor(data: str) -> AllocationStatus:
    return cast(AllocationStatus, data)
