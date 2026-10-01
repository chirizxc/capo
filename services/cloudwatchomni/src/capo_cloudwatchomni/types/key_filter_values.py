"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#KeyFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.key_filter_value

KeyFilterValues: TypeAlias = list[
    "capo_cloudwatchomni.types.key_filter_value.KeyFilterValue"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: KeyFilterValues) -> list:
    return list(value)


def deserialize_cbor(data: list) -> KeyFilterValues:
    return [item for item in data if item is not None]
