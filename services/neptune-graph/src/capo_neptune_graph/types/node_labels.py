"""Generated from Smithy shape ``com.amazonaws.neptunegraph#NodeLabels``."""

from typing import TypeAlias

NodeLabels: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: NodeLabels) -> list:
    return list(value)


def deserialize_json(data: list) -> NodeLabels:
    return [item for item in data if item is not None]
