"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ProductCodeList``."""

from typing import TypeAlias

ProductCodeList: TypeAlias = list["str"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProductCodeList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ProductCodeList:
    return [item for item in data if item is not None]
