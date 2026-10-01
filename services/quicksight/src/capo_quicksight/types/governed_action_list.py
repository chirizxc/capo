"""Generated from Smithy shape ``com.amazonaws.quicksight#GovernedActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.governed_action

GovernedActionList: TypeAlias = list[
    "capo_quicksight.types.governed_action.GovernedAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: GovernedActionList) -> list:
    import capo_quicksight.types.governed_action

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.governed_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> GovernedActionList:
    import capo_quicksight.types.governed_action

    out: GovernedActionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.governed_action.deserialize_json(item))
    return out
