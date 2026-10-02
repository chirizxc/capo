"""Generated from Smithy shape ``com.amazonaws.connect#GetCrossRegionRoutingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.isolated_regions_list


class GetCrossRegionRoutingResponse(TypedDict, closed=True):
    isolated_regions: NotRequired[
        "capo_connect.types.isolated_regions_list.IsolatedRegionsList"
    ]
    """<p>The list of Regions for which cross-region routing is currently disabled (isolated). When a Region appears in this list, contacts originating in that Region will not be routed to agents in other Regions, and agents in that Region will not receive contacts from other Regions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCrossRegionRoutingResponse) -> dict:
    out: dict = {}
    if "isolated_regions" in value:
        import capo_connect.types.isolated_regions_list

        out["IsolatedRegions"] = (
            capo_connect.types.isolated_regions_list.serialize_json(
                value["isolated_regions"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetCrossRegionRoutingResponse:
    out: GetCrossRegionRoutingResponse = {}  # type: ignore[typeddict-item]
    if data.get("IsolatedRegions") is not None:
        import capo_connect.types.isolated_regions_list

        out["isolated_regions"] = (
            capo_connect.types.isolated_regions_list.deserialize_json(
                data["IsolatedRegions"]
            )
        )
    return out
