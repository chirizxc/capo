"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#NodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.node

NodeList: TypeAlias = list["capo_cloudwatchomni.types.node.Node"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NodeList) -> list:
    import capo_cloudwatchomni.types.node

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.node.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> NodeList:
    import capo_cloudwatchomni.types.node

    out: NodeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.node.deserialize_cbor(item))
    return out
