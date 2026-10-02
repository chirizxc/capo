"""Generated from Smithy shape ``com.amazonaws.launchwizard#WorkloadDeploymentPatternDataSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_launch_wizard.types.account_constraints_list
    import capo_launch_wizard.types.deployment_pattern_name
    import capo_launch_wizard.types.deployment_pattern_version_name
    import capo_launch_wizard.types.workload_deployment_pattern_status
    import capo_launch_wizard.types.workload_name
    import capo_launch_wizard.types.workload_version_name


class WorkloadDeploymentPatternDataSummary(TypedDict, closed=True):
    workload_name: NotRequired["capo_launch_wizard.types.workload_name.WorkloadName"]
    """<p>The name of the workload.</p>"""
    deployment_pattern_name: NotRequired[
        "capo_launch_wizard.types.deployment_pattern_name.DeploymentPatternName"
    ]
    """<p>The name of a workload deployment pattern.</p>"""
    workload_version_name: NotRequired[
        "capo_launch_wizard.types.workload_version_name.WorkloadVersionName"
    ]
    """<p>The name of the workload deployment pattern version.</p>"""
    deployment_pattern_version_name: NotRequired[
        "capo_launch_wizard.types.deployment_pattern_version_name.DeploymentPatternVersionName"
    ]
    """<p>The version name of a workload deployment pattern.</p>"""
    display_name: NotRequired["str"]
    """<p>The display name of a workload deployment pattern.</p>"""
    description: NotRequired["str"]
    """<p>The description of a workload deployment pattern.</p>"""
    status: NotRequired[
        "capo_launch_wizard.types.workload_deployment_pattern_status.WorkloadDeploymentPatternStatus"
    ]
    """<p>The status of a workload deployment pattern.</p>"""
    status_message: NotRequired["str"]
    """<p>A message about a workload deployment pattern's status.</p>"""
    account_constraints: NotRequired[
        "capo_launch_wizard.types.account_constraints_list.AccountConstraintsList"
    ]
    """Optional list of constraints describing what kind of AWS account is allowed to deploy this workload or deployment pattern. Within a single list the semantics are OR: an account satisfies the list if it satisfies any entry. Workload-level and pattern-level lists combine with AND at deployment time. An absent or empty list at this level means no constraint at this level."""


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadDeploymentPatternDataSummary) -> dict:
    out: dict = {}
    if "workload_name" in value:
        out["workloadName"] = value["workload_name"]
    if "deployment_pattern_name" in value:
        out["deploymentPatternName"] = value["deployment_pattern_name"]
    if "workload_version_name" in value:
        out["workloadVersionName"] = value["workload_version_name"]
    if "deployment_pattern_version_name" in value:
        out["deploymentPatternVersionName"] = value["deployment_pattern_version_name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import capo_launch_wizard.types.workload_deployment_pattern_status

        out["status"] = (
            capo_launch_wizard.types.workload_deployment_pattern_status.serialize_json(
                value["status"]
            )
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "account_constraints" in value:
        import capo_launch_wizard.types.account_constraints_list

        out["accountConstraints"] = (
            capo_launch_wizard.types.account_constraints_list.serialize_json(
                value["account_constraints"]
            )
        )
    return out


def deserialize_json(data: dict) -> WorkloadDeploymentPatternDataSummary:
    out: WorkloadDeploymentPatternDataSummary = {}  # type: ignore[typeddict-item]
    if data.get("workloadName") is not None:
        out["workload_name"] = data["workloadName"]
    if data.get("deploymentPatternName") is not None:
        out["deployment_pattern_name"] = data["deploymentPatternName"]
    if data.get("workloadVersionName") is not None:
        out["workload_version_name"] = data["workloadVersionName"]
    if data.get("deploymentPatternVersionName") is not None:
        out["deployment_pattern_version_name"] = data["deploymentPatternVersionName"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_launch_wizard.types.workload_deployment_pattern_status

        out["status"] = (
            capo_launch_wizard.types.workload_deployment_pattern_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("accountConstraints") is not None:
        import capo_launch_wizard.types.account_constraints_list

        out["account_constraints"] = (
            capo_launch_wizard.types.account_constraints_list.deserialize_json(
                data["accountConstraints"]
            )
        )
    return out
