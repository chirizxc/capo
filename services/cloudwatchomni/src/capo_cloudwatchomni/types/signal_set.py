"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#SignalSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.signal

SignalSet: TypeAlias = list["capo_cloudwatchomni.types.signal.Signal"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SignalSet) -> list:
    import capo_cloudwatchomni.types.signal

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.signal.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SignalSet:
    import capo_cloudwatchomni.types.signal

    out: SignalSet = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.signal.deserialize_cbor(item))
    return out
