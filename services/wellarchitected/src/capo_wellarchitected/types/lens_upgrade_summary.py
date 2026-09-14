"""Generated from Smithy shape ``com.amazonaws.wellarchitected#LensUpgradeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.lens_alias
    import capo_wellarchitected.types.lens_arn
    import capo_wellarchitected.types.lens_version
    import capo_wellarchitected.types.resource_arn
    import capo_wellarchitected.types.workload_id
    import capo_wellarchitected.types.workload_name


class LensUpgradeSummary(TypedDict, closed=True):
    workload_id: NotRequired["capo_wellarchitected.types.workload_id.WorkloadId"]
    workload_name: NotRequired["capo_wellarchitected.types.workload_name.WorkloadName"]
    lens_alias: NotRequired["capo_wellarchitected.types.lens_alias.LensAlias"]
    lens_arn: NotRequired["capo_wellarchitected.types.lens_arn.LensArn"]
    """<p>The ARN for the lens.</p>"""
    current_lens_version: NotRequired[
        "capo_wellarchitected.types.lens_version.LensVersion"
    ]
    """<p>The current version of the lens.</p>"""
    latest_lens_version: NotRequired[
        "capo_wellarchitected.types.lens_version.LensVersion"
    ]
    """<p>The latest version of the lens.</p>"""
    resource_arn: NotRequired["capo_wellarchitected.types.resource_arn.ResourceArn"]
    """<p> <code>ResourceArn</code> of the lens being upgraded</p>"""
    resource_name: NotRequired["capo_wellarchitected.types.workload_name.WorkloadName"]


# --- restJson1 ser/de ---
def serialize_json(value: LensUpgradeSummary) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "workload_name" in value:
        out["WorkloadName"] = value["workload_name"]
    if "lens_alias" in value:
        out["LensAlias"] = value["lens_alias"]
    if "lens_arn" in value:
        out["LensArn"] = value["lens_arn"]
    if "current_lens_version" in value:
        out["CurrentLensVersion"] = value["current_lens_version"]
    if "latest_lens_version" in value:
        out["LatestLensVersion"] = value["latest_lens_version"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> LensUpgradeSummary:
    out: LensUpgradeSummary = {}  # type: ignore[typeddict-item]
    if data.get("WorkloadId") is not None:
        out["workload_id"] = data["WorkloadId"]
    if data.get("WorkloadName") is not None:
        out["workload_name"] = data["WorkloadName"]
    if data.get("LensAlias") is not None:
        out["lens_alias"] = data["LensAlias"]
    if data.get("LensArn") is not None:
        out["lens_arn"] = data["LensArn"]
    if data.get("CurrentLensVersion") is not None:
        out["current_lens_version"] = data["CurrentLensVersion"]
    if data.get("LatestLensVersion") is not None:
        out["latest_lens_version"] = data["LatestLensVersion"]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("ResourceName") is not None:
        out["resource_name"] = data["ResourceName"]
    return out
