"""Generated from Smithy shape ``com.amazonaws.eks#ResourceWeight``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.resource_weight_name
    import capo_eks.types.resource_weight_value


class ResourceWeight(TypedDict, closed=True):
    name: NotRequired["capo_eks.types.resource_weight_name.ResourceWeightName"]
    """<p>The name of the resource (for example, <code>cpu</code> or <code>memory</code>).</p>"""
    weight: NotRequired["capo_eks.types.resource_weight_value.ResourceWeightValue"]
    """<p>The weight assigned to the resource for scoring. Must be between 1 and 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceWeight) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "weight" in value:
        out["weight"] = value["weight"]
    return out


def deserialize_json(data: dict) -> ResourceWeight:
    out: ResourceWeight = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("weight") is not None:
        out["weight"] = data["weight"]
    return out
