"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveMemoryMetadataFilterOperator``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the relationship that a metadata key and value must have for a memory record to match a filter expression.</p>"""
AgenticRetrieveMemoryMetadataFilterOperator: TypeAlias = Literal[
    "EQUALS_TO",
    "EXISTS",
    "NOT_EXISTS",
    "BEFORE",
    "AFTER",
    "CONTAINS",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUALS",
    "LESS_THAN",
    "LESS_THAN_OR_EQUALS",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveMemoryMetadataFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> AgenticRetrieveMemoryMetadataFilterOperator:
    return cast(AgenticRetrieveMemoryMetadataFilterOperator, data)
