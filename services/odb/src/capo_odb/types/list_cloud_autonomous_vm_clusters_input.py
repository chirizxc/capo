"""Generated from Smithy shape ``com.amazonaws.odb#ListCloudAutonomousVmClustersInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id_or_arn


class ListCloudAutonomousVmClustersInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of items to return per page.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token to continue listing from.</p>"""
    cloud_exadata_infrastructure_id: NotRequired[
        "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    ]
    """<p>The unique identifier of the Cloud Exadata Infrastructure that hosts the Autonomous VM clusters to be listed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListCloudAutonomousVmClustersInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "cloud_exadata_infrastructure_id" in value:
        out["cloudExadataInfrastructureId"] = value["cloud_exadata_infrastructure_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListCloudAutonomousVmClustersInput:
    out: ListCloudAutonomousVmClustersInput = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("cloudExadataInfrastructureId") is not None:
        out["cloud_exadata_infrastructure_id"] = data["cloudExadataInfrastructureId"]
    return out
