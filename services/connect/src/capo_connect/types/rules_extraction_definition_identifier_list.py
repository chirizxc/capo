"""Generated from Smithy shape ``com.amazonaws.connect#RulesExtractionDefinitionIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.rules_extraction_definition_identifier

RulesExtractionDefinitionIdentifierList: TypeAlias = list[
    "capo_connect.types.rules_extraction_definition_identifier.RulesExtractionDefinitionIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: RulesExtractionDefinitionIdentifierList) -> list:
    import capo_connect.types.rules_extraction_definition_identifier

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.rules_extraction_definition_identifier.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RulesExtractionDefinitionIdentifierList:
    import capo_connect.types.rules_extraction_definition_identifier

    out: RulesExtractionDefinitionIdentifierList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connect.types.rules_extraction_definition_identifier.deserialize_json(
                item
            )
        )
    return out
