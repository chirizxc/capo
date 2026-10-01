"""Generated from Smithy shape ``com.amazonaws.securityagent#UpdateSecurityRequirementEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.update_security_requirement_entry

UpdateSecurityRequirementEntryList: TypeAlias = list[
    "capo_securityagent.types.update_security_requirement_entry.UpdateSecurityRequirementEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSecurityRequirementEntryList) -> list:
    import capo_securityagent.types.update_security_requirement_entry

    out: list = []
    for item in value:
        out.append(
            capo_securityagent.types.update_security_requirement_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> UpdateSecurityRequirementEntryList:
    import capo_securityagent.types.update_security_requirement_entry

    out: UpdateSecurityRequirementEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityagent.types.update_security_requirement_entry.deserialize_json(
                item
            )
        )
    return out
