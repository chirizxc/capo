"""Generated from Smithy shape ``com.amazonaws.neptunedata#Predicates``."""

from typing import TypeAlias

Predicates: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: Predicates) -> list:
    return list(value)


def deserialize_json(data: list) -> Predicates:
    return [item for item in data if item is not None]
