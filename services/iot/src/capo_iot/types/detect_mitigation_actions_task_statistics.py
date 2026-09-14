"""Generated from Smithy shape ``com.amazonaws.iot#DetectMitigationActionsTaskStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.generic_long_value


class DetectMitigationActionsTaskStatistics(TypedDict, closed=True):
    actions_executed: NotRequired["capo_iot.types.generic_long_value.GenericLongValue"]
    """<p> The actions that were performed. </p>"""
    actions_skipped: NotRequired["capo_iot.types.generic_long_value.GenericLongValue"]
    """<p> The actions that were skipped. </p>"""
    actions_failed: NotRequired["capo_iot.types.generic_long_value.GenericLongValue"]
    """<p> The actions that failed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectMitigationActionsTaskStatistics) -> dict:
    out: dict = {}
    if "actions_executed" in value:
        out["actionsExecuted"] = value["actions_executed"]
    if "actions_skipped" in value:
        out["actionsSkipped"] = value["actions_skipped"]
    if "actions_failed" in value:
        out["actionsFailed"] = value["actions_failed"]
    return out


def deserialize_json(data: dict) -> DetectMitigationActionsTaskStatistics:
    out: DetectMitigationActionsTaskStatistics = {}  # type: ignore[typeddict-item]
    if data.get("actionsExecuted") is not None:
        out["actions_executed"] = data["actionsExecuted"]
    if data.get("actionsSkipped") is not None:
        out["actions_skipped"] = data["actionsSkipped"]
    if data.get("actionsFailed") is not None:
        out["actions_failed"] = data["actionsFailed"]
    return out
