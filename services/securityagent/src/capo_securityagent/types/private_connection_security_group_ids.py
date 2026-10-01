"""Generated from Smithy shape ``com.amazonaws.securityagent#PrivateConnectionSecurityGroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.private_connection_security_group_id

PrivateConnectionSecurityGroupIds: TypeAlias = list[
    "capo_securityagent.types.private_connection_security_group_id.PrivateConnectionSecurityGroupId"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivateConnectionSecurityGroupIds) -> list:
    return list(value)


def deserialize_json(data: list) -> PrivateConnectionSecurityGroupIds:
    return [item for item in data if item is not None]
