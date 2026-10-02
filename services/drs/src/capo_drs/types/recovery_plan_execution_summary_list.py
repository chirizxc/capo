"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryPlanExecutionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.recovery_plan_execution_summary

RecoveryPlanExecutionSummaryList: TypeAlias = list[
    "capo_drs.types.recovery_plan_execution_summary.RecoveryPlanExecutionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPlanExecutionSummaryList) -> list:
    import capo_drs.types.recovery_plan_execution_summary

    out: list = []
    for item in value:
        out.append(capo_drs.types.recovery_plan_execution_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecoveryPlanExecutionSummaryList:
    import capo_drs.types.recovery_plan_execution_summary

    out: RecoveryPlanExecutionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_drs.types.recovery_plan_execution_summary.deserialize_json(item)
        )
    return out
