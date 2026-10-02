"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#EntityType``."""

from typing import Literal, TypeAlias, cast

EntityType: TypeAlias = Literal[
    "OFFER",
    "OPPORTUNITY",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntityType) -> str:
    return value


def deserialize_cbor(data: str) -> EntityType:
    return cast(EntityType, data)
