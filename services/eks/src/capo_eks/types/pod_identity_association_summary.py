"""Generated from Smithy shape ``com.amazonaws.eks#PodIdentityAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string


class PodIdentityAssociationSummary(TypedDict, closed=True):
    cluster_name: NotRequired["capo_eks.types.string.String"]
    """<p>The name of the cluster that the association is in.</p>"""
    namespace: NotRequired["capo_eks.types.string.String"]
    """<p>The name of the Kubernetes namespace inside the cluster to create the association in. The service account and the Pods that use the service account must be in this namespace.</p>"""
    service_account: NotRequired["capo_eks.types.string.String"]
    """<p>The name of the Kubernetes service account inside the cluster to associate the IAM credentials with.</p>"""
    association_arn: NotRequired["capo_eks.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the association.</p>"""
    association_id: NotRequired["capo_eks.types.string.String"]
    """<p>The ID of the association.</p>"""
    owner_arn: NotRequired["capo_eks.types.string.String"]
    """<p>If defined, the association is owned by an Amazon EKS add-on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PodIdentityAssociationSummary) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "service_account" in value:
        out["serviceAccount"] = value["service_account"]
    if "association_arn" in value:
        out["associationArn"] = value["association_arn"]
    if "association_id" in value:
        out["associationId"] = value["association_id"]
    if "owner_arn" in value:
        out["ownerArn"] = value["owner_arn"]
    return out


def deserialize_json(data: dict) -> PodIdentityAssociationSummary:
    out: PodIdentityAssociationSummary = {}  # type: ignore[typeddict-item]
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    if data.get("serviceAccount") is not None:
        out["service_account"] = data["serviceAccount"]
    if data.get("associationArn") is not None:
        out["association_arn"] = data["associationArn"]
    if data.get("associationId") is not None:
        out["association_id"] = data["associationId"]
    if data.get("ownerArn") is not None:
        out["owner_arn"] = data["ownerArn"]
    return out
