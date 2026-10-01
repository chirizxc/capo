"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#NodeType``."""

from typing import Literal, TypeAlias, cast

"""Context graph node types."""
NodeType: TypeAlias = Literal[
    "SERVICE",
    "RESOURCE",
    "REMOTE_SERVICE",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NodeType) -> str:
    return value


def deserialize_cbor(data: str) -> NodeType:
    return cast(NodeType, data)
