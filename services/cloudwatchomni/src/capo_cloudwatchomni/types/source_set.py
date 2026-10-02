"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#SourceSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.source

SourceSet: TypeAlias = list["capo_cloudwatchomni.types.source.Source"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SourceSet) -> list:
    import capo_cloudwatchomni.types.source

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.source.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SourceSet:
    import capo_cloudwatchomni.types.source

    out: SourceSet = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.source.deserialize_cbor(item))
    return out
