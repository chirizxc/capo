"""Generated from Smithy shape ``com.amazonaws.sagemaker#AttachClusterNodeNetworkInterfaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_arn
    import capo_sagemaker.types.cluster_network_interface_attachment_id
    import capo_sagemaker.types.cluster_network_interface_id
    import capo_sagemaker.types.cluster_node_id


class AttachClusterNodeNetworkInterfaceResponse(TypedDict, closed=True):
    cluster_arn: NotRequired["capo_sagemaker.types.cluster_arn.ClusterArn"]
    """<p> The Amazon Resource Name (ARN) of your SageMaker HyperPod cluster where the network interface attachment operation was performed. </p>"""
    node_id: NotRequired["capo_sagemaker.types.cluster_node_id.ClusterNodeId"]
    """<p> The unique identifier of the cluster node where your network interface was attached. </p>"""
    network_interface_id: NotRequired[
        "capo_sagemaker.types.cluster_network_interface_id.ClusterNetworkInterfaceId"
    ]
    """<p> The unique identifier of the elastic network interface (ENI) that was attached. </p>"""
    attachment_id: NotRequired[
        "capo_sagemaker.types.cluster_network_interface_attachment_id.ClusterNetworkInterfaceAttachmentId"
    ]
    """<p> The unique identifier of the network interface attachment. Use this value to reference or detach the network interface later. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachClusterNodeNetworkInterfaceResponse) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "node_id" in value:
        out["NodeId"] = value["node_id"]
    if "network_interface_id" in value:
        out["NetworkInterfaceId"] = value["network_interface_id"]
    if "attachment_id" in value:
        out["AttachmentId"] = value["attachment_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachClusterNodeNetworkInterfaceResponse:
    out: AttachClusterNodeNetworkInterfaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("ClusterArn") is not None:
        out["cluster_arn"] = data["ClusterArn"]
    if data.get("NodeId") is not None:
        out["node_id"] = data["NodeId"]
    if data.get("NetworkInterfaceId") is not None:
        out["network_interface_id"] = data["NetworkInterfaceId"]
    if data.get("AttachmentId") is not None:
        out["attachment_id"] = data["AttachmentId"]
    return out
