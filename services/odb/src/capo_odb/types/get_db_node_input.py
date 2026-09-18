"""Generated from Smithy shape ``com.amazonaws.odb#GetDbNodeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_odb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_odb.types.resource_id


class GetDbNodeInput(TypedDict, closed=True):
    cloud_vm_cluster_id: "capo_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the VM cluster that contains the DB node.</p>"""
    db_node_id: "capo_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the DB node to retrieve information about.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDbNodeInput) -> dict:
    out: dict = {}
    out["cloudVmClusterId"] = value["cloud_vm_cluster_id"]
    out["dbNodeId"] = value["db_node_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDbNodeInput:
    out: GetDbNodeInput = {}  # type: ignore[typeddict-item]
    if data.get("cloudVmClusterId") is not None:
        out["cloud_vm_cluster_id"] = data["cloudVmClusterId"]
    else:
        raise DeserializationError("GetDbNodeInput.cloud_vm_cluster_id required")
    if data.get("dbNodeId") is not None:
        out["db_node_id"] = data["dbNodeId"]
    else:
        raise DeserializationError("GetDbNodeInput.db_node_id required")
    return out
