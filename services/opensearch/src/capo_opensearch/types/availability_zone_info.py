"""Generated from Smithy shape ``com.amazonaws.opensearch#AvailabilityZoneInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.availability_zone
    import capo_opensearch.types.number_of_nodes
    import capo_opensearch.types.number_of_shards
    import capo_opensearch.types.zone_status


class AvailabilityZoneInfo(TypedDict, closed=True):
    availability_zone_name: NotRequired[
        "capo_opensearch.types.availability_zone.AvailabilityZone"
    ]
    """<p>The name of the Availability Zone.</p>"""
    zone_status: NotRequired["capo_opensearch.types.zone_status.ZoneStatus"]
    """<p>The current state of the Availability Zone. Current options are <code>Active</code> and <code>StandBy</code>.</p> <ul> <li> <p> <code>Active</code> - Data nodes in the Availability Zone are in use.</p> </li> <li> <p> <code>StandBy</code> - Data nodes in the Availability Zone are in a standby state.</p> </li> <li> <p> <code>NotAvailable</code> - Unable to retrieve information.</p> </li> </ul>"""
    configured_data_node_count: NotRequired[
        "capo_opensearch.types.number_of_nodes.NumberOfNodes"
    ]
    """<p>The total number of data nodes configured in the Availability Zone.</p>"""
    available_data_node_count: NotRequired[
        "capo_opensearch.types.number_of_nodes.NumberOfNodes"
    ]
    """<p>The number of data nodes active in the Availability Zone.</p>"""
    total_shards: NotRequired["capo_opensearch.types.number_of_shards.NumberOfShards"]
    """<p>The total number of primary and replica shards in the Availability Zone.</p>"""
    total_un_assigned_shards: NotRequired[
        "capo_opensearch.types.number_of_shards.NumberOfShards"
    ]
    """<p>The total number of primary and replica shards that aren't allocated to any of the nodes in the Availability Zone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AvailabilityZoneInfo) -> dict:
    out: dict = {}
    if "availability_zone_name" in value:
        out["AvailabilityZoneName"] = value["availability_zone_name"]
    if "zone_status" in value:
        import capo_opensearch.types.zone_status

        out["ZoneStatus"] = capo_opensearch.types.zone_status.serialize_json(
            value["zone_status"]
        )
    if "configured_data_node_count" in value:
        out["ConfiguredDataNodeCount"] = value["configured_data_node_count"]
    if "available_data_node_count" in value:
        out["AvailableDataNodeCount"] = value["available_data_node_count"]
    if "total_shards" in value:
        out["TotalShards"] = value["total_shards"]
    if "total_un_assigned_shards" in value:
        out["TotalUnAssignedShards"] = value["total_un_assigned_shards"]
    return out


def deserialize_json(data: dict) -> AvailabilityZoneInfo:
    out: AvailabilityZoneInfo = {}  # type: ignore[typeddict-item]
    if data.get("AvailabilityZoneName") is not None:
        out["availability_zone_name"] = data["AvailabilityZoneName"]
    if data.get("ZoneStatus") is not None:
        import capo_opensearch.types.zone_status

        out["zone_status"] = capo_opensearch.types.zone_status.deserialize_json(
            data["ZoneStatus"]
        )
    if data.get("ConfiguredDataNodeCount") is not None:
        out["configured_data_node_count"] = data["ConfiguredDataNodeCount"]
    if data.get("AvailableDataNodeCount") is not None:
        out["available_data_node_count"] = data["AvailableDataNodeCount"]
    if data.get("TotalShards") is not None:
        out["total_shards"] = data["TotalShards"]
    if data.get("TotalUnAssignedShards") is not None:
        out["total_un_assigned_shards"] = data["TotalUnAssignedShards"]
    return out
