"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ChildResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.child_resource

ChildResourceList: TypeAlias = list[
    "capo_cleanrooms.types.child_resource.ChildResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChildResourceList) -> list:
    import capo_cleanrooms.types.child_resource

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.child_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChildResourceList:
    import capo_cleanrooms.types.child_resource

    out: ChildResourceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cleanrooms.types.child_resource.deserialize_json(item))
    return out
