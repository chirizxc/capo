"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#PointType``."""

from typing import Literal, TypeAlias, cast

PointType: TypeAlias = Literal[
    "HORIZON",
    "TIMESTAMP",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PointType) -> str:
    return value


def deserialize_cbor(data: str) -> PointType:
    return cast(PointType, data)
