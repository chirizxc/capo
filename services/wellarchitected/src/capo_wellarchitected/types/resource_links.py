"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ResourceLinks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.resource_link

ResourceLinks: TypeAlias = list["capo_wellarchitected.types.resource_link.ResourceLink"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceLinks) -> list:
    import capo_wellarchitected.types.resource_link

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.resource_link.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceLinks:
    import capo_wellarchitected.types.resource_link

    out: ResourceLinks = []
    for item in data:
        if item is None:
            continue
        out.append(capo_wellarchitected.types.resource_link.deserialize_json(item))
    return out
