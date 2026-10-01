"""Generated from Smithy shape ``com.amazonaws.guardduty#ActivityType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of an observed activity.</p>"""
ActivityType: TypeAlias = Literal["API_CALL",]


# --- restJson1 ser/de ---
def serialize_json(value: ActivityType) -> str:
    return value


def deserialize_json(data: str) -> ActivityType:
    return cast(ActivityType, data)
