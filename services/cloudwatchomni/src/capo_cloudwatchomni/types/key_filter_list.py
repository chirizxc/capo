"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#KeyFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.key_filter

KeyFilterList: TypeAlias = list["capo_cloudwatchomni.types.key_filter.KeyFilter"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: KeyFilterList) -> list:
    import capo_cloudwatchomni.types.key_filter

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.key_filter.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> KeyFilterList:
    import capo_cloudwatchomni.types.key_filter

    out: KeyFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.key_filter.deserialize_cbor(item))
    return out
