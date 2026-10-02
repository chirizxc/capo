"""Generated from Smithy shape ``com.amazonaws.eks#EtcdPlacementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.spread_level


class EtcdPlacementRequest(TypedDict, closed=True):
    spread_level: NotRequired["capo_eks.types.spread_level.SpreadLevel"]
    """<p>Optional parameter to specify the placement group spread level for etcd instances. If not provided, Amazon EKS will deploy etcd instances without a placement group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EtcdPlacementRequest) -> dict:
    out: dict = {}
    if "spread_level" in value:
        import capo_eks.types.spread_level

        out["spreadLevel"] = capo_eks.types.spread_level.serialize_json(
            value["spread_level"]
        )
    return out


def deserialize_json(data: dict) -> EtcdPlacementRequest:
    out: EtcdPlacementRequest = {}  # type: ignore[typeddict-item]
    if data.get("spreadLevel") is not None:
        import capo_eks.types.spread_level

        out["spread_level"] = capo_eks.types.spread_level.deserialize_json(
            data["spreadLevel"]
        )
    return out
