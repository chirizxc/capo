"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputeNodeNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.resource_name

ComputeNodeNameList: TypeAlias = list[
    "capo_iotsitewise.types.resource_name.ResourceName"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComputeNodeNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> ComputeNodeNameList:
    return [item for item in data if item is not None]
