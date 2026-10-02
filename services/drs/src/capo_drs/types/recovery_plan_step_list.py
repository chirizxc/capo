"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryPlanStepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.recovery_plan_step

RecoveryPlanStepList: TypeAlias = list[
    "capo_drs.types.recovery_plan_step.RecoveryPlanStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPlanStepList) -> list:
    import capo_drs.types.recovery_plan_step

    out: list = []
    for item in value:
        out.append(capo_drs.types.recovery_plan_step.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecoveryPlanStepList:
    import capo_drs.types.recovery_plan_step

    out: RecoveryPlanStepList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_drs.types.recovery_plan_step.deserialize_json(item))
    return out
