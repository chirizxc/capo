"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#CatalogName``."""

from typing import Literal, TypeAlias, cast

CatalogName: TypeAlias = Literal[
    "AWS",
    "Sandbox",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CatalogName) -> str:
    return value


def deserialize_cbor(data: str) -> CatalogName:
    return cast(CatalogName, data)
