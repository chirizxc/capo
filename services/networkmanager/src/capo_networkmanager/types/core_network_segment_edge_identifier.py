"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkSegmentEdgeIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.external_region_code


class CoreNetworkSegmentEdgeIdentifier(TypedDict, closed=True):
    core_network_id: NotRequired[
        "capo_networkmanager.types.core_network_id.CoreNetworkId"
    ]
    """<p>The ID of a core network.</p>"""
    segment_name: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The name of the segment edge.</p>"""
    edge_location: NotRequired[
        "capo_networkmanager.types.external_region_code.ExternalRegionCode"
    ]
    """<p>The Region where the segment edge is located.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkSegmentEdgeIdentifier) -> dict:
    out: dict = {}
    if "core_network_id" in value:
        out["CoreNetworkId"] = value["core_network_id"]
    if "segment_name" in value:
        out["SegmentName"] = value["segment_name"]
    if "edge_location" in value:
        out["EdgeLocation"] = value["edge_location"]
    return out


def deserialize_json(data: dict) -> CoreNetworkSegmentEdgeIdentifier:
    out: CoreNetworkSegmentEdgeIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("CoreNetworkId") is not None:
        out["core_network_id"] = data["CoreNetworkId"]
    if data.get("SegmentName") is not None:
        out["segment_name"] = data["SegmentName"]
    if data.get("EdgeLocation") is not None:
        out["edge_location"] = data["EdgeLocation"]
    return out
