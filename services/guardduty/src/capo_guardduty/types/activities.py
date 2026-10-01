"""Generated from Smithy shape ``com.amazonaws.guardduty#Activities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.activity

Activities: TypeAlias = list["capo_guardduty.types.activity.Activity"]


# --- restJson1 ser/de ---
def serialize_json(value: Activities) -> list:
    import capo_guardduty.types.activity

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.activity.serialize_json(item))
    return out


def deserialize_json(data: list) -> Activities:
    import capo_guardduty.types.activity

    out: Activities = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.activity.deserialize_json(item))
    return out
