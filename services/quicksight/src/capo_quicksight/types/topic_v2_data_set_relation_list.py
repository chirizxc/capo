"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicV2DataSetRelationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.topic_v2_data_set_relation

TopicV2DataSetRelationList: TypeAlias = list[
    "capo_quicksight.types.topic_v2_data_set_relation.TopicV2DataSetRelation"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicV2DataSetRelationList) -> list:
    import capo_quicksight.types.topic_v2_data_set_relation

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.topic_v2_data_set_relation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TopicV2DataSetRelationList:
    import capo_quicksight.types.topic_v2_data_set_relation

    out: TopicV2DataSetRelationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.topic_v2_data_set_relation.deserialize_json(item)
        )
    return out
