"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#AssociatedFieldsList``."""

from typing import TypeAlias

AssociatedFieldsList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedFieldsList) -> list:
    return list(value)


def deserialize_json(data: list) -> AssociatedFieldsList:
    return [item for item in data if item is not None]
