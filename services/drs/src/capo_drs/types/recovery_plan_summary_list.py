"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryPlanSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.recovery_plan_summary

RecoveryPlanSummaryList: TypeAlias = list[
    "capo_drs.types.recovery_plan_summary.RecoveryPlanSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPlanSummaryList) -> list:
    import capo_drs.types.recovery_plan_summary

    out: list = []
    for item in value:
        out.append(capo_drs.types.recovery_plan_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecoveryPlanSummaryList:
    import capo_drs.types.recovery_plan_summary

    out: RecoveryPlanSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_drs.types.recovery_plan_summary.deserialize_json(item))
    return out
