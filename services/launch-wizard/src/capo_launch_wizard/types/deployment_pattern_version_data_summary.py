"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentPatternVersionDataSummary``."""

from typing_extensions import NotRequired, TypedDict


class DeploymentPatternVersionDataSummary(TypedDict, closed=True):
    deployment_pattern_version_name: NotRequired["str"]
    """<p>The name of the deployment pattern version.</p>"""
    description: NotRequired["str"]
    """<p>The description of the deployment pattern version.</p>"""
    documentation_url: NotRequired["str"]
    """<p>The URL of the documentation for the deployment pattern version.</p>"""
    workload_name: NotRequired["str"]
    """<p>The name of the workload.</p>"""
    deployment_pattern_name: NotRequired["str"]
    """<p>The name of the deployment pattern.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentPatternVersionDataSummary) -> dict:
    out: dict = {}
    if "deployment_pattern_version_name" in value:
        out["deploymentPatternVersionName"] = value["deployment_pattern_version_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "documentation_url" in value:
        out["documentationUrl"] = value["documentation_url"]
    if "workload_name" in value:
        out["workloadName"] = value["workload_name"]
    if "deployment_pattern_name" in value:
        out["deploymentPatternName"] = value["deployment_pattern_name"]
    return out


def deserialize_json(data: dict) -> DeploymentPatternVersionDataSummary:
    out: DeploymentPatternVersionDataSummary = {}  # type: ignore[typeddict-item]
    if data.get("deploymentPatternVersionName") is not None:
        out["deployment_pattern_version_name"] = data["deploymentPatternVersionName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("documentationUrl") is not None:
        out["documentation_url"] = data["documentationUrl"]
    if data.get("workloadName") is not None:
        out["workload_name"] = data["workloadName"]
    if data.get("deploymentPatternName") is not None:
        out["deployment_pattern_name"] = data["deploymentPatternName"]
    return out
