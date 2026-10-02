"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AlertNameFilterList``."""

from typing import TypeAlias

AlertNameFilterList: TypeAlias = list["str"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlertNameFilterList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> AlertNameFilterList:
    return [item for item in data if item is not None]
