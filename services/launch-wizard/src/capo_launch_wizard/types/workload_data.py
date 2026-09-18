"""Generated from Smithy shape ``com.amazonaws.launchwizard#WorkloadData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_launch_wizard.types.workload_name
    import capo_launch_wizard.types.workload_status


class WorkloadData(TypedDict, closed=True):
    workload_name: NotRequired["capo_launch_wizard.types.workload_name.WorkloadName"]
    """<p>The name of the workload.</p>"""
    display_name: NotRequired["str"]
    """<p>The display name of a workload.</p>"""
    status: NotRequired["capo_launch_wizard.types.workload_status.WorkloadStatus"]
    """<p>The status of a workload.</p> <p> <i>You can list deployments in the <code>DISABLED</code> status.</i> </p>"""
    description: NotRequired["str"]
    """<p>The description of a workload.</p>"""
    documentation_url: NotRequired["str"]
    """<p>The URL of a workload document.</p>"""
    icon_url: NotRequired["str"]
    """<p>The URL of a workload icon.</p>"""
    status_message: NotRequired["str"]
    """<p>The message about a workload's status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadData) -> dict:
    out: dict = {}
    if "workload_name" in value:
        out["workloadName"] = value["workload_name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "status" in value:
        import capo_launch_wizard.types.workload_status

        out["status"] = capo_launch_wizard.types.workload_status.serialize_json(
            value["status"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "documentation_url" in value:
        out["documentationUrl"] = value["documentation_url"]
    if "icon_url" in value:
        out["iconUrl"] = value["icon_url"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> WorkloadData:
    out: WorkloadData = {}  # type: ignore[typeddict-item]
    if data.get("workloadName") is not None:
        out["workload_name"] = data["workloadName"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("status") is not None:
        import capo_launch_wizard.types.workload_status

        out["status"] = capo_launch_wizard.types.workload_status.deserialize_json(
            data["status"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("documentationUrl") is not None:
        out["documentation_url"] = data["documentationUrl"]
    if data.get("iconUrl") is not None:
        out["icon_url"] = data["iconUrl"]
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    return out
