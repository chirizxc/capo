"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ResolvedTargetResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.resolved_target_resource

ResolvedTargetResourceList: TypeAlias = list[
    "capo_resiliencehubv2.types.resolved_target_resource.ResolvedTargetResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResolvedTargetResourceList) -> list:
    import capo_resiliencehubv2.types.resolved_target_resource

    out: list = []
    for item in value:
        out.append(
            capo_resiliencehubv2.types.resolved_target_resource.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ResolvedTargetResourceList:
    import capo_resiliencehubv2.types.resolved_target_resource

    out: ResolvedTargetResourceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_resiliencehubv2.types.resolved_target_resource.deserialize_json(item)
        )
    return out
