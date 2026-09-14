"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListStageDevicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.boolean
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.list_max_results
    import capo_sagemaker.types.next_token


class ListStageDevicesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>The response from the last list when returning a list large enough to neeed tokening.</p>"""
    max_results: NotRequired["capo_sagemaker.types.list_max_results.ListMaxResults"]
    """<p>The maximum number of requests to select.</p>"""
    edge_deployment_plan_name: NotRequired[
        "capo_sagemaker.types.entity_name.EntityName"
    ]
    """<p>The name of the edge deployment plan.</p>"""
    exclude_devices_deployed_in_other_stage: NotRequired[
        "capo_sagemaker.types.boolean.Boolean"
    ]
    """<p>Toggle for excluding devices deployed in other stages.</p>"""
    stage_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the stage in the deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStageDevicesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "edge_deployment_plan_name" in value:
        out["EdgeDeploymentPlanName"] = value["edge_deployment_plan_name"]
    if "exclude_devices_deployed_in_other_stage" in value:
        out["ExcludeDevicesDeployedInOtherStage"] = value[
            "exclude_devices_deployed_in_other_stage"
        ]
    if "stage_name" in value:
        out["StageName"] = value["stage_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStageDevicesRequest:
    out: ListStageDevicesRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("EdgeDeploymentPlanName") is not None:
        out["edge_deployment_plan_name"] = data["EdgeDeploymentPlanName"]
    if data.get("ExcludeDevicesDeployedInOtherStage") is not None:
        out["exclude_devices_deployed_in_other_stage"] = data[
            "ExcludeDevicesDeployedInOtherStage"
        ]
    if data.get("StageName") is not None:
        out["stage_name"] = data["StageName"]
    return out
