"""Generated from Smithy shape ``com.amazonaws.wickr#SecurityGroupIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wickr.types.security_group_id

SecurityGroupIdList: TypeAlias = list[
    "capo_wickr.types.security_group_id.SecurityGroupId"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> SecurityGroupIdList:
    return [item for item in data if item is not None]
