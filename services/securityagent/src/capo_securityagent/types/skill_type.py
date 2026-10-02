"""Generated from Smithy shape ``com.amazonaws.securityagent#SkillType``."""

from typing import Literal, TypeAlias, cast

"""<p>Type of managed skill that can be enabled or disabled for a pentest.</p>"""
SkillType: TypeAlias = Literal[
    "FINDING_PERSONALIZATION",
    "LOGIN_OPTIMIZATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: SkillType) -> str:
    return value


def deserialize_json(data: str) -> SkillType:
    return cast(SkillType, data)
