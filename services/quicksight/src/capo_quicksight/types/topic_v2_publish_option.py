"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicV2PublishOption``."""

from typing import Literal, TypeAlias, cast

TopicV2PublishOption: TypeAlias = Literal[
    "DRAFT",
    "PUBLISH",
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicV2PublishOption) -> str:
    return value


def deserialize_json(data: str) -> TopicV2PublishOption:
    return cast(TopicV2PublishOption, data)
