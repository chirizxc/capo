"""Generated from Smithy shape ``com.amazonaws.sagemaker#AttachClusterNodeNetworkInterfaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_name_or_arn
    import capo_sagemaker.types.cluster_network_interface_id
    import capo_sagemaker.types.cluster_node_id


class AttachClusterNodeNetworkInterfaceRequest(TypedDict, closed=True):
    cluster_name: NotRequired[
        "capo_sagemaker.types.cluster_name_or_arn.ClusterNameOrArn"
    ]
    """<p> The name or Amazon Resource Name (ARN) of the SageMaker HyperPod cluster that contains the target node. </p>"""
    node_id: NotRequired["capo_sagemaker.types.cluster_node_id.ClusterNodeId"]
    """<p> The unique identifier of the cluster node to which you want to attach the network interface. The node must belong to your specified HyperPod cluster and cannot be part of a Restricted Instance Group (RIG). </p>"""
    network_interface_id: NotRequired[
        "capo_sagemaker.types.cluster_network_interface_id.ClusterNetworkInterfaceId"
    ]
    """<p> The unique identifier of the elastic network interface (ENI) to attach. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachClusterNodeNetworkInterfaceRequest) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "node_id" in value:
        out["NodeId"] = value["node_id"]
    if "network_interface_id" in value:
        out["NetworkInterfaceId"] = value["network_interface_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachClusterNodeNetworkInterfaceRequest:
    out: AttachClusterNodeNetworkInterfaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    if data.get("NodeId") is not None:
        out["node_id"] = data["NodeId"]
    if data.get("NetworkInterfaceId") is not None:
        out["network_interface_id"] = data["NetworkInterfaceId"]
    return out
