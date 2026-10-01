"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CompositeIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.composite_identifier_entry

CompositeIdentifierList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.composite_identifier_entry.CompositeIdentifierEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: CompositeIdentifierList) -> list:
    return list(value)


def deserialize_json(data: list) -> CompositeIdentifierList:
    return [item for item in data if item is not None]
