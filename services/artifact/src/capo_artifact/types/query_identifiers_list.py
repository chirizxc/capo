"""Generated from Smithy shape ``com.amazonaws.artifact#QueryIdentifiersList``."""

from typing import TypeAlias

QueryIdentifiersList: TypeAlias = list["int"]


# --- restJson1 ser/de ---
def serialize_json(value: QueryIdentifiersList) -> list:
    return list(value)


def deserialize_json(data: list) -> QueryIdentifiersList:
    return [item for item in data if item is not None]
