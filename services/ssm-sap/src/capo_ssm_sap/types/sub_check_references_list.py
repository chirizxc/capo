"""Generated from Smithy shape ``com.amazonaws.ssmsap#SubCheckReferencesList``."""

from typing import TypeAlias

SubCheckReferencesList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: SubCheckReferencesList) -> list:
    return list(value)


def deserialize_json(data: list) -> SubCheckReferencesList:
    return [item for item in data if item is not None]
