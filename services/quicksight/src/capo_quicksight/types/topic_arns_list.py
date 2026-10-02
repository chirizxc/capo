"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicArnsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.arn

TopicArnsList: TypeAlias = list["capo_quicksight.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: TopicArnsList) -> list:
    return list(value)


def deserialize_json(data: list) -> TopicArnsList:
    return [item for item in data if item is not None]
