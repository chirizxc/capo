"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#SignalTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.signal_type

SignalTypeList: TypeAlias = list["capo_cloudwatchomni.types.signal_type.SignalType"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SignalTypeList) -> list:
    import capo_cloudwatchomni.types.signal_type

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.signal_type.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SignalTypeList:
    import capo_cloudwatchomni.types.signal_type

    out: SignalTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.signal_type.deserialize_cbor(item))
    return out
