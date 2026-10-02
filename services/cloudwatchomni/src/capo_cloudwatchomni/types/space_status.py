"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#SpaceStatus``."""

from typing import Literal, TypeAlias, cast

"""Status of a space."""
SpaceStatus: TypeAlias = Literal[
    "ACTIVE",
    "SUSPENDED",
    "MOVING",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SpaceStatus) -> str:
    return value


def deserialize_cbor(data: str) -> SpaceStatus:
    return cast(SpaceStatus, data)
