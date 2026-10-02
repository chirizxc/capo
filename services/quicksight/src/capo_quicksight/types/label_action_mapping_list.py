"""Generated from Smithy shape ``com.amazonaws.quicksight#LabelActionMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.label_action_mapping

LabelActionMappingList: TypeAlias = list[
    "capo_quicksight.types.label_action_mapping.LabelActionMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: LabelActionMappingList) -> list:
    import capo_quicksight.types.label_action_mapping

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.label_action_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> LabelActionMappingList:
    import capo_quicksight.types.label_action_mapping

    out: LabelActionMappingList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.label_action_mapping.deserialize_json(item))
    return out
