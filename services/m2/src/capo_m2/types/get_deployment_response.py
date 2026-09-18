"""Generated from Smithy shape ``com.amazonaws.m2#GetDeploymentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_m2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_m2.types.deployment_lifecycle
    import capo_m2.types.identifier
    import capo_m2.types.timestamp
    import capo_m2.types.version


class GetDeploymentResponse(TypedDict, closed=True):
    deployment_id: "capo_m2.types.identifier.Identifier"
    """<p>The unique identifier of the deployment.</p>"""
    application_id: "capo_m2.types.identifier.Identifier"
    """<p>The unique identifier of the application.</p>"""
    environment_id: "capo_m2.types.identifier.Identifier"
    """<p>The unique identifier of the runtime environment.</p>"""
    application_version: "capo_m2.types.version.Version"
    """<p>The application version.</p>"""
    status: "capo_m2.types.deployment_lifecycle.DeploymentLifecycle"
    """<p>The status of the deployment.</p>"""
    creation_time: "capo_m2.types.timestamp.Timestamp"
    """<p>The timestamp when the deployment was created.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the reported status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeploymentResponse) -> dict:
    out: dict = {}
    out["deploymentId"] = value["deployment_id"]
    out["applicationId"] = value["application_id"]
    out["environmentId"] = value["environment_id"]
    out["applicationVersion"] = value["application_version"]
    out["status"] = value["status"]
    import capo_m2.types.timestamp

    out["creationTime"] = capo_m2.types.timestamp.serialize_json(value["creation_time"])
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> GetDeploymentResponse:
    out: GetDeploymentResponse = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    else:
        raise DeserializationError("GetDeploymentResponse.deployment_id required")
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("GetDeploymentResponse.application_id required")
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError("GetDeploymentResponse.environment_id required")
    if data.get("applicationVersion") is not None:
        out["application_version"] = data["applicationVersion"]
    else:
        raise DeserializationError("GetDeploymentResponse.application_version required")
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetDeploymentResponse.status required")
    if data.get("creationTime") is not None:
        import capo_m2.types.timestamp

        out["creation_time"] = capo_m2.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("GetDeploymentResponse.creation_time required")
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    return out
