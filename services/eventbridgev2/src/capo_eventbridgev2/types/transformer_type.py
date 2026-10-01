"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#TransformerType``."""

from typing import Literal, TypeAlias, cast

TransformerType: TypeAlias = Literal[
    "RAW",
    "WITH_METADATA",
    "JSONATA",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TransformerType) -> str:
    return value


def deserialize_cbor(data: str) -> TransformerType:
    return cast(TransformerType, data)
