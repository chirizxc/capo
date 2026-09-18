"""Generated from Smithy shape ``com.amazonaws.drs#LaunchActionRun``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.failure_reason
    import capo_drs.types.launch_action
    import capo_drs.types.launch_action_run_id
    import capo_drs.types.launch_action_run_status


class LaunchActionRun(TypedDict, closed=True):
    action: NotRequired["capo_drs.types.launch_action.LaunchAction"]
    """<p>Action.</p>"""
    run_id: NotRequired["capo_drs.types.launch_action_run_id.LaunchActionRunId"]
    """<p>Run Id.</p>"""
    status: NotRequired["capo_drs.types.launch_action_run_status.LaunchActionRunStatus"]
    """<p>Run status.</p>"""
    failure_reason: NotRequired["capo_drs.types.failure_reason.FailureReason"]
    """<p>Failure reason.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LaunchActionRun) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_drs.types.launch_action

        out["action"] = capo_drs.types.launch_action.serialize_json(value["action"])
    if "run_id" in value:
        out["runId"] = value["run_id"]
    if "status" in value:
        out["status"] = value["status"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> LaunchActionRun:
    out: LaunchActionRun = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        import capo_drs.types.launch_action

        out["action"] = capo_drs.types.launch_action.deserialize_json(data["action"])
    if data.get("runId") is not None:
        out["run_id"] = data["runId"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    return out
