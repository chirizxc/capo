"""Generated from Smithy shape ``com.amazonaws.securityagent#SecurityRequirementNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.security_requirement_name

SecurityRequirementNameList: TypeAlias = list[
    "capo_securityagent.types.security_requirement_name.SecurityRequirementName"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityRequirementNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> SecurityRequirementNameList:
    return [item for item in data if item is not None]
