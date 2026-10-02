"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.topic_reference

TopicReferenceList: TypeAlias = list[
    "capo_quicksight.types.topic_reference.TopicReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicReferenceList) -> list:
    import capo_quicksight.types.topic_reference

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.topic_reference.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicReferenceList:
    import capo_quicksight.types.topic_reference

    out: TopicReferenceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.topic_reference.deserialize_json(item))
    return out
