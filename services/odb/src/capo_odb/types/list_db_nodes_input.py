"""Generated from Smithy shape ``com.amazonaws.odb#ListDbNodesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id


class ListDbNodesInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>"""
    next_token: NotRequired["str"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    cloud_vm_cluster_id: NotRequired["capo_odb.types.resource_id.ResourceId"]
    """<p>The unique identifier of the VM cluster. You must specify either this parameter or <code>exadbVmClusterId</code>.</p>"""
    exadb_vm_cluster_id: NotRequired["capo_odb.types.resource_id.ResourceId"]
    """<p>The unique identifier of the Exascale VM cluster. You must specify either this parameter or <code>cloudVmClusterId</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDbNodesInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "cloud_vm_cluster_id" in value:
        out["cloudVmClusterId"] = value["cloud_vm_cluster_id"]
    if "exadb_vm_cluster_id" in value:
        out["exadbVmClusterId"] = value["exadb_vm_cluster_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDbNodesInput:
    out: ListDbNodesInput = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("cloudVmClusterId") is not None:
        out["cloud_vm_cluster_id"] = data["cloudVmClusterId"]
    if data.get("exadbVmClusterId") is not None:
        out["exadb_vm_cluster_id"] = data["exadbVmClusterId"]
    return out
