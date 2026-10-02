"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#NodeCategorySet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.node_category

NodeCategorySet: TypeAlias = list[
    "capo_cloudwatchomni.types.node_category.NodeCategory"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NodeCategorySet) -> list:
    import capo_cloudwatchomni.types.node_category

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.node_category.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> NodeCategorySet:
    import capo_cloudwatchomni.types.node_category

    out: NodeCategorySet = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.node_category.deserialize_cbor(item))
    return out
