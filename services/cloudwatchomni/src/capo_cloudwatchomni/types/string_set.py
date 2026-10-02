"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#StringSet``."""

from typing import TypeAlias

StringSet: TypeAlias = list["str"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StringSet) -> list:
    return list(value)


def deserialize_cbor(data: list) -> StringSet:
    return [item for item in data if item is not None]
