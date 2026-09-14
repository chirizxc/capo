"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#RelatedModelFieldsList``."""

from typing import TypeAlias

RelatedModelFieldsList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: RelatedModelFieldsList) -> list:
    return list(value)


def deserialize_json(data: list) -> RelatedModelFieldsList:
    return [item for item in data if item is not None]
