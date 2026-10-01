"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.topic_configuration

TopicConfigurationList: TypeAlias = list[
    "capo_quicksight.types.topic_configuration.TopicConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicConfigurationList) -> list:
    import capo_quicksight.types.topic_configuration

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.topic_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicConfigurationList:
    import capo_quicksight.types.topic_configuration

    out: TopicConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.topic_configuration.deserialize_json(item))
    return out
