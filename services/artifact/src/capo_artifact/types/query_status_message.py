"""Generated from Smithy shape ``com.amazonaws.artifact#QueryStatusMessage``."""

from typing import Literal, TypeAlias, cast

QueryStatusMessage: TypeAlias = Literal[
    "Query processing is complete.",
    "Query processing is in-progress.",
    "An internal error occurred while processing the query. Try again at a later time.",
    "Query is pending human review.",
    "Query contains restricted or unsupported content.",
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryStatusMessage) -> str:
    return value


def deserialize_json(data: str) -> QueryStatusMessage:
    return cast(QueryStatusMessage, data)
