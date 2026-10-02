"""Generated from Smithy shape ``com.amazonaws.eks#EtcdPlacementResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.spread_level


class EtcdPlacementResponse(TypedDict, closed=True):
    spread_level: NotRequired["capo_eks.types.spread_level.SpreadLevel"]
    """<p>The spread level used with the placement group for etcd instances on your local Amazon EKS cluster on Amazon Web Services Outposts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EtcdPlacementResponse) -> dict:
    out: dict = {}
    if "spread_level" in value:
        import capo_eks.types.spread_level

        out["spreadLevel"] = capo_eks.types.spread_level.serialize_json(
            value["spread_level"]
        )
    return out


def deserialize_json(data: dict) -> EtcdPlacementResponse:
    out: EtcdPlacementResponse = {}  # type: ignore[typeddict-item]
    if data.get("spreadLevel") is not None:
        import capo_eks.types.spread_level

        out["spread_level"] = capo_eks.types.spread_level.deserialize_json(
            data["spreadLevel"]
        )
    return out
