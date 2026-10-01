"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#EdgeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.edge

EdgeList: TypeAlias = list["capo_cloudwatchomni.types.edge.Edge"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EdgeList) -> list:
    import capo_cloudwatchomni.types.edge

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.edge.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EdgeList:
    import capo_cloudwatchomni.types.edge

    out: EdgeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.edge.deserialize_cbor(item))
    return out
