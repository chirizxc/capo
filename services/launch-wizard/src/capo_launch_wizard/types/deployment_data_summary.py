"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentDataSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_launch_wizard.types.deployment_id
    import capo_launch_wizard.types.deployment_pattern_name
    import capo_launch_wizard.types.deployment_status
    import capo_launch_wizard.types.workload_name


class DeploymentDataSummary(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the deployment</p>"""
    id: NotRequired["capo_launch_wizard.types.deployment_id.DeploymentId"]
    """<p>The ID of the deployment.</p>"""
    workload_name: NotRequired["capo_launch_wizard.types.workload_name.WorkloadName"]
    """<p>The name of the workload.</p>"""
    pattern_name: NotRequired[
        "capo_launch_wizard.types.deployment_pattern_name.DeploymentPatternName"
    ]
    """<p>The name of the workload deployment pattern.</p>"""
    status: NotRequired["capo_launch_wizard.types.deployment_status.DeploymentStatus"]
    """<p>The status of the deployment.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The time the deployment was created.</p>"""
    modified_at: NotRequired["datetime.datetime"]
    """<p>The time the deployment was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentDataSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "id" in value:
        out["id"] = value["id"]
    if "workload_name" in value:
        out["workloadName"] = value["workload_name"]
    if "pattern_name" in value:
        out["patternName"] = value["pattern_name"]
    if "status" in value:
        import capo_launch_wizard.types.deployment_status

        out["status"] = capo_launch_wizard.types.deployment_status.serialize_json(
            value["status"]
        )
    if "created_at" in value:
        import capo_launch_wizard.types._prelude.timestamp

        out["createdAt"] = capo_launch_wizard.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "modified_at" in value:
        import capo_launch_wizard.types._prelude.timestamp

        out["modifiedAt"] = capo_launch_wizard.types._prelude.timestamp.serialize_json(
            value["modified_at"]
        )
    return out


def deserialize_json(data: dict) -> DeploymentDataSummary:
    out: DeploymentDataSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("workloadName") is not None:
        out["workload_name"] = data["workloadName"]
    if data.get("patternName") is not None:
        out["pattern_name"] = data["patternName"]
    if data.get("status") is not None:
        import capo_launch_wizard.types.deployment_status

        out["status"] = capo_launch_wizard.types.deployment_status.deserialize_json(
            data["status"]
        )
    if data.get("createdAt") is not None:
        import capo_launch_wizard.types._prelude.timestamp

        out["created_at"] = (
            capo_launch_wizard.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if data.get("modifiedAt") is not None:
        import capo_launch_wizard.types._prelude.timestamp

        out["modified_at"] = (
            capo_launch_wizard.types._prelude.timestamp.deserialize_json(
                data["modifiedAt"]
            )
        )
    return out
