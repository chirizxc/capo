"""Generated from Smithy shape ``com.amazonaws.eks#ControlPlanePlacementResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.spread_level
    import capo_eks.types.string


class ControlPlanePlacementResponse(TypedDict, closed=True):
    group_name: NotRequired["capo_eks.types.string.String"]
    """<p>The name of the placement group for the Kubernetes control plane instances.</p>"""
    spread_level: NotRequired["capo_eks.types.spread_level.SpreadLevel"]
    """<p>The spread level used with the placement group for control plane instances on your local Amazon EKS cluster on Amazon Web Services Outposts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlPlanePlacementResponse) -> dict:
    out: dict = {}
    if "group_name" in value:
        out["groupName"] = value["group_name"]
    if "spread_level" in value:
        import capo_eks.types.spread_level

        out["spreadLevel"] = capo_eks.types.spread_level.serialize_json(
            value["spread_level"]
        )
    return out


def deserialize_json(data: dict) -> ControlPlanePlacementResponse:
    out: ControlPlanePlacementResponse = {}  # type: ignore[typeddict-item]
    if data.get("groupName") is not None:
        out["group_name"] = data["groupName"]
    if data.get("spreadLevel") is not None:
        import capo_eks.types.spread_level

        out["spread_level"] = capo_eks.types.spread_level.deserialize_json(
            data["spreadLevel"]
        )
    return out
