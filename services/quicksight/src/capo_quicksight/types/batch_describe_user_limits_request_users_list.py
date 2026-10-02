"""Generated from Smithy shape ``com.amazonaws.quicksight#BatchDescribeUserLimitsRequestUsersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.user_limits_entry

BatchDescribeUserLimitsRequestUsersList: TypeAlias = list[
    "capo_quicksight.types.user_limits_entry.UserLimitsEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDescribeUserLimitsRequestUsersList) -> list:
    import capo_quicksight.types.user_limits_entry

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.user_limits_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchDescribeUserLimitsRequestUsersList:
    import capo_quicksight.types.user_limits_entry

    out: BatchDescribeUserLimitsRequestUsersList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.user_limits_entry.deserialize_json(item))
    return out
