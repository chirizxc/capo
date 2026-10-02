"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicIdentifierDeclarationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.topic_identifier_declaration

TopicIdentifierDeclarationList: TypeAlias = list[
    "capo_quicksight.types.topic_identifier_declaration.TopicIdentifierDeclaration"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicIdentifierDeclarationList) -> list:
    import capo_quicksight.types.topic_identifier_declaration

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.topic_identifier_declaration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TopicIdentifierDeclarationList:
    import capo_quicksight.types.topic_identifier_declaration

    out: TopicIdentifierDeclarationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.topic_identifier_declaration.deserialize_json(item)
        )
    return out
