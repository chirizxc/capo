"""Generated from Smithy shape ``com.amazonaws.drs#UpdateRecoveryPlanStepResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_drs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_drs.types.recovery_plan_step


class UpdateRecoveryPlanStepResponse(TypedDict, closed=True):
    recovery_plan_step: "capo_drs.types.recovery_plan_step.RecoveryPlanStep"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecoveryPlanStepResponse) -> dict:
    out: dict = {}
    import capo_drs.types.recovery_plan_step

    out["recoveryPlanStep"] = capo_drs.types.recovery_plan_step.serialize_json(
        value["recovery_plan_step"]
    )
    return out


def deserialize_json(data: dict) -> UpdateRecoveryPlanStepResponse:
    out: UpdateRecoveryPlanStepResponse = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanStep") is not None:
        import capo_drs.types.recovery_plan_step

        out["recovery_plan_step"] = capo_drs.types.recovery_plan_step.deserialize_json(
            data["recoveryPlanStep"]
        )
    else:
        raise DeserializationError(
            "UpdateRecoveryPlanStepResponse.recovery_plan_step required"
        )
    return out
