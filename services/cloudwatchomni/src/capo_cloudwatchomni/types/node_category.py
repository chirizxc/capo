"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#NodeCategory``."""

from typing import Literal, TypeAlias, cast

"""Coarse classification of what a node is. Orthogonal to NodeType, which says whether the node is a service, a resource, or a remote service. Absent on most nodes today because few producers emit the source attribute."""
NodeCategory: TypeAlias = Literal[
    "GEN_AI_AGENT",
    "GEN_AI_MODEL",
    "DATABASE",
    "MESSAGING_QUEUE",
    "COMPUTE",
    "STORAGE",
    "NETWORK",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NodeCategory) -> str:
    return value


def deserialize_cbor(data: str) -> NodeCategory:
    return cast(NodeCategory, data)
