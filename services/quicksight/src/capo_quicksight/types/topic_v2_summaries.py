"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicV2Summaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.topic_v2_summary

TopicV2Summaries: TypeAlias = list[
    "capo_quicksight.types.topic_v2_summary.TopicV2Summary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicV2Summaries) -> list:
    import capo_quicksight.types.topic_v2_summary

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.topic_v2_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicV2Summaries:
    import capo_quicksight.types.topic_v2_summary

    out: TopicV2Summaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.topic_v2_summary.deserialize_json(item))
    return out
