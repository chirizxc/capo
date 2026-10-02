"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ClientRoutingPolicy``."""

from typing import Literal, TypeAlias, cast

ClientRoutingPolicy: TypeAlias = Literal[
    "AVAILABILITY_ZONE_AFFINITY",
    "ANY_AVAILABILITY_ZONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ClientRoutingPolicy) -> str:
    return value


def deserialize_json(data: str) -> ClientRoutingPolicy:
    return cast(ClientRoutingPolicy, data)
