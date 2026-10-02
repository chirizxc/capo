"""Generated from Smithy shape ``com.amazonaws.eks#ControlPlaneScalingTierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.control_plane_scaling_tier_info

ControlPlaneScalingTierList: TypeAlias = list[
    "capo_eks.types.control_plane_scaling_tier_info.ControlPlaneScalingTierInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlPlaneScalingTierList) -> list:
    import capo_eks.types.control_plane_scaling_tier_info

    out: list = []
    for item in value:
        out.append(capo_eks.types.control_plane_scaling_tier_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> ControlPlaneScalingTierList:
    import capo_eks.types.control_plane_scaling_tier_info

    out: ControlPlaneScalingTierList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_eks.types.control_plane_scaling_tier_info.deserialize_json(item)
        )
    return out
