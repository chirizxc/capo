"""Generated from Smithy shape ``com.amazonaws.greengrass#BulkDeploymentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string
    import capo_greengrass.types.deployment_type
    import capo_greengrass.types.error_details


class BulkDeploymentResult(TypedDict, closed=True):
    created_at: NotRequired["capo_greengrass.types.__string.__string"]
    """The time, in ISO format, when the deployment was created."""
    deployment_arn: NotRequired["capo_greengrass.types.__string.__string"]
    """The ARN of the group deployment."""
    deployment_id: NotRequired["capo_greengrass.types.__string.__string"]
    """The ID of the group deployment."""
    deployment_status: NotRequired["capo_greengrass.types.__string.__string"]
    """The current status of the group deployment: ''InProgress'', ''Building'', ''Success'', or ''Failure''."""
    deployment_type: NotRequired["capo_greengrass.types.deployment_type.DeploymentType"]
    """The type of the deployment."""
    error_details: NotRequired["capo_greengrass.types.error_details.ErrorDetails"]
    """Details about the error."""
    error_message: NotRequired["capo_greengrass.types.__string.__string"]
    """The error message for a failed deployment"""
    group_arn: NotRequired["capo_greengrass.types.__string.__string"]
    """The ARN of the Greengrass group."""


# --- restJson1 ser/de ---
def serialize_json(value: BulkDeploymentResult) -> dict:
    out: dict = {}
    if "created_at" in value:
        out["CreatedAt"] = value["created_at"]
    if "deployment_arn" in value:
        out["DeploymentArn"] = value["deployment_arn"]
    if "deployment_id" in value:
        out["DeploymentId"] = value["deployment_id"]
    if "deployment_status" in value:
        out["DeploymentStatus"] = value["deployment_status"]
    if "deployment_type" in value:
        import capo_greengrass.types.deployment_type

        out["DeploymentType"] = capo_greengrass.types.deployment_type.serialize_json(
            value["deployment_type"]
        )
    if "error_details" in value:
        import capo_greengrass.types.error_details

        out["ErrorDetails"] = capo_greengrass.types.error_details.serialize_json(
            value["error_details"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "group_arn" in value:
        out["GroupArn"] = value["group_arn"]
    return out


def deserialize_json(data: dict) -> BulkDeploymentResult:
    out: BulkDeploymentResult = {}  # type: ignore[typeddict-item]
    if data.get("CreatedAt") is not None:
        out["created_at"] = data["CreatedAt"]
    if data.get("DeploymentArn") is not None:
        out["deployment_arn"] = data["DeploymentArn"]
    if data.get("DeploymentId") is not None:
        out["deployment_id"] = data["DeploymentId"]
    if data.get("DeploymentStatus") is not None:
        out["deployment_status"] = data["DeploymentStatus"]
    if data.get("DeploymentType") is not None:
        import capo_greengrass.types.deployment_type

        out["deployment_type"] = capo_greengrass.types.deployment_type.deserialize_json(
            data["DeploymentType"]
        )
    if data.get("ErrorDetails") is not None:
        import capo_greengrass.types.error_details

        out["error_details"] = capo_greengrass.types.error_details.deserialize_json(
            data["ErrorDetails"]
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("GroupArn") is not None:
        out["group_arn"] = data["GroupArn"]
    return out
