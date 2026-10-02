"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryPlanExecutionStepSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.recovery_plan_execution_step_summary

RecoveryPlanExecutionStepSummaryList: TypeAlias = list[
    "capo_drs.types.recovery_plan_execution_step_summary.RecoveryPlanExecutionStepSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPlanExecutionStepSummaryList) -> list:
    import capo_drs.types.recovery_plan_execution_step_summary

    out: list = []
    for item in value:
        out.append(
            capo_drs.types.recovery_plan_execution_step_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RecoveryPlanExecutionStepSummaryList:
    import capo_drs.types.recovery_plan_execution_step_summary

    out: RecoveryPlanExecutionStepSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_drs.types.recovery_plan_execution_step_summary.deserialize_json(item)
        )
    return out
