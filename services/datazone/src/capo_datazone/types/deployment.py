"""Generated from Smithy shape ``com.amazonaws.datazone#Deployment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.deployment_messages_list
    import capo_datazone.types.deployment_status
    import capo_datazone.types.deployment_type
    import capo_datazone.types.environment_error


class Deployment(TypedDict, closed=True):
    deployment_id: NotRequired["str"]
    """<p>The identifier of the last deployment of the environment.</p>"""
    deployment_type: NotRequired["capo_datazone.types.deployment_type.DeploymentType"]
    """<p>The type of the last deployment of the environment.</p>"""
    deployment_status: NotRequired[
        "capo_datazone.types.deployment_status.DeploymentStatus"
    ]
    """<p>The status of the last deployment of the environment.</p>"""
    failure_reason: NotRequired[
        "capo_datazone.types.environment_error.EnvironmentError"
    ]
    """<p>The failure reason of the last deployment of the environment.</p>"""
    messages: NotRequired[
        "capo_datazone.types.deployment_messages_list.DeploymentMessagesList"
    ]
    """<p>The messages of the last deployment of the environment.</p>"""
    is_deployment_complete: NotRequired["bool"]
    """<p>Specifies whether the last deployment of the environment is complete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Deployment) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "deployment_type" in value:
        import capo_datazone.types.deployment_type

        out["deploymentType"] = capo_datazone.types.deployment_type.serialize_json(
            value["deployment_type"]
        )
    if "deployment_status" in value:
        import capo_datazone.types.deployment_status

        out["deploymentStatus"] = capo_datazone.types.deployment_status.serialize_json(
            value["deployment_status"]
        )
    if "failure_reason" in value:
        import capo_datazone.types.environment_error

        out["failureReason"] = capo_datazone.types.environment_error.serialize_json(
            value["failure_reason"]
        )
    if "messages" in value:
        import capo_datazone.types.deployment_messages_list

        out["messages"] = capo_datazone.types.deployment_messages_list.serialize_json(
            value["messages"]
        )
    if "is_deployment_complete" in value:
        out["isDeploymentComplete"] = value["is_deployment_complete"]
    return out


def deserialize_json(data: dict) -> Deployment:
    out: Deployment = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    if data.get("deploymentType") is not None:
        import capo_datazone.types.deployment_type

        out["deployment_type"] = capo_datazone.types.deployment_type.deserialize_json(
            data["deploymentType"]
        )
    if data.get("deploymentStatus") is not None:
        import capo_datazone.types.deployment_status

        out["deployment_status"] = (
            capo_datazone.types.deployment_status.deserialize_json(
                data["deploymentStatus"]
            )
        )
    if data.get("failureReason") is not None:
        import capo_datazone.types.environment_error

        out["failure_reason"] = capo_datazone.types.environment_error.deserialize_json(
            data["failureReason"]
        )
    if data.get("messages") is not None:
        import capo_datazone.types.deployment_messages_list

        out["messages"] = capo_datazone.types.deployment_messages_list.deserialize_json(
            data["messages"]
        )
    if data.get("isDeploymentComplete") is not None:
        out["is_deployment_complete"] = data["isDeploymentComplete"]
    return out
