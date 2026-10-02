"""Generated from Smithy shape ``com.amazonaws.drs#ListRecoveryPlanExecutionStepsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.recovery_plan_execution_step_status


class ListRecoveryPlanExecutionStepsFilter(TypedDict, closed=True):
    status: NotRequired[
        "capo_drs.types.recovery_plan_execution_step_status.RecoveryPlanExecutionStepStatus"
    ]
    """<p>Filter by execution step status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecoveryPlanExecutionStepsFilter) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> ListRecoveryPlanExecutionStepsFilter:
    out: ListRecoveryPlanExecutionStepsFilter = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    return out
