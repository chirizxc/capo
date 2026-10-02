"""Generated from Smithy shape ``com.amazonaws.securityagent#PrivateConnectionSubnetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.private_connection_subnet_id

PrivateConnectionSubnetIds: TypeAlias = list[
    "capo_securityagent.types.private_connection_subnet_id.PrivateConnectionSubnetId"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivateConnectionSubnetIds) -> list:
    return list(value)


def deserialize_json(data: list) -> PrivateConnectionSubnetIds:
    return [item for item in data if item is not None]
