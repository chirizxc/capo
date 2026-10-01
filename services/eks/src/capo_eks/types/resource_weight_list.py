"""Generated from Smithy shape ``com.amazonaws.eks#ResourceWeightList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.resource_weight

ResourceWeightList: TypeAlias = list["capo_eks.types.resource_weight.ResourceWeight"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceWeightList) -> list:
    import capo_eks.types.resource_weight

    out: list = []
    for item in value:
        out.append(capo_eks.types.resource_weight.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceWeightList:
    import capo_eks.types.resource_weight

    out: ResourceWeightList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_eks.types.resource_weight.deserialize_json(item))
    return out
