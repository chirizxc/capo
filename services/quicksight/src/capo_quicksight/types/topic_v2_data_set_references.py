"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicV2DataSetReferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.topic_v2_data_set_reference

TopicV2DataSetReferences: TypeAlias = list[
    "capo_quicksight.types.topic_v2_data_set_reference.TopicV2DataSetReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicV2DataSetReferences) -> list:
    import capo_quicksight.types.topic_v2_data_set_reference

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.topic_v2_data_set_reference.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TopicV2DataSetReferences:
    import capo_quicksight.types.topic_v2_data_set_reference

    out: TopicV2DataSetReferences = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.topic_v2_data_set_reference.deserialize_json(item)
        )
    return out
