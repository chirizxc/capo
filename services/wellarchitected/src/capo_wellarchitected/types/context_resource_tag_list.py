"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ContextResourceTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.context_resource_tag

ContextResourceTagList: TypeAlias = list[
    "capo_wellarchitected.types.context_resource_tag.ContextResourceTag"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContextResourceTagList) -> list:
    import capo_wellarchitected.types.context_resource_tag

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.context_resource_tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContextResourceTagList:
    import capo_wellarchitected.types.context_resource_tag

    out: ContextResourceTagList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wellarchitected.types.context_resource_tag.deserialize_json(item)
        )
    return out
