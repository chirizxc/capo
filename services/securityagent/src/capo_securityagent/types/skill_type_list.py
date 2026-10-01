"""Generated from Smithy shape ``com.amazonaws.securityagent#SkillTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.skill_type

SkillTypeList: TypeAlias = list["capo_securityagent.types.skill_type.SkillType"]


# --- restJson1 ser/de ---
def serialize_json(value: SkillTypeList) -> list:
    import capo_securityagent.types.skill_type

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.skill_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> SkillTypeList:
    import capo_securityagent.types.skill_type

    out: SkillTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityagent.types.skill_type.deserialize_json(item))
    return out
