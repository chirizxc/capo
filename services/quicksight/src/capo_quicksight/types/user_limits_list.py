"""Generated from Smithy shape ``com.amazonaws.quicksight#UserLimitsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.user_limits

UserLimitsList: TypeAlias = list["capo_quicksight.types.user_limits.UserLimits"]


# --- restJson1 ser/de ---
def serialize_json(value: UserLimitsList) -> list:
    import capo_quicksight.types.user_limits

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.user_limits.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserLimitsList:
    import capo_quicksight.types.user_limits

    out: UserLimitsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.user_limits.deserialize_json(item))
    return out
