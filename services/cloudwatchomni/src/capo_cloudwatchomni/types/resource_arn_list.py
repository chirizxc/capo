"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ResourceArnList``."""

from typing import TypeAlias

ResourceArnList: TypeAlias = list["str"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceArnList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ResourceArnList:
    return [item for item in data if item is not None]
