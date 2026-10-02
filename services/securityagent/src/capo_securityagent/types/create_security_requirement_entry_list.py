"""Generated from Smithy shape ``com.amazonaws.securityagent#CreateSecurityRequirementEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.create_security_requirement_entry

CreateSecurityRequirementEntryList: TypeAlias = list[
    "capo_securityagent.types.create_security_requirement_entry.CreateSecurityRequirementEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateSecurityRequirementEntryList) -> list:
    import capo_securityagent.types.create_security_requirement_entry

    out: list = []
    for item in value:
        out.append(
            capo_securityagent.types.create_security_requirement_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CreateSecurityRequirementEntryList:
    import capo_securityagent.types.create_security_requirement_entry

    out: CreateSecurityRequirementEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityagent.types.create_security_requirement_entry.deserialize_json(
                item
            )
        )
    return out
