"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfTopicConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafka.types.topic_configuration

__listOfTopicConfiguration: TypeAlias = list[
    "capo_kafka.types.topic_configuration.TopicConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfTopicConfiguration) -> list:
    import capo_kafka.types.topic_configuration

    out: list = []
    for item in value:
        out.append(capo_kafka.types.topic_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfTopicConfiguration:
    import capo_kafka.types.topic_configuration

    out: __listOfTopicConfiguration = []
    for item in data:
        if item is None:
            continue
        out.append(capo_kafka.types.topic_configuration.deserialize_json(item))
    return out
