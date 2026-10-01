"""Generated from Smithy shape ``com.amazonaws.drs#RetryRecoveryPlanExecutionStepResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_drs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_drs.types.recovery_plan_execution_step


class RetryRecoveryPlanExecutionStepResponse(TypedDict, closed=True):
    recovery_plan_execution_step: (
        "capo_drs.types.recovery_plan_execution_step.RecoveryPlanExecutionStep"
    )


# --- restJson1 ser/de ---
def serialize_json(value: RetryRecoveryPlanExecutionStepResponse) -> dict:
    out: dict = {}
    import capo_drs.types.recovery_plan_execution_step

    out["recoveryPlanExecutionStep"] = (
        capo_drs.types.recovery_plan_execution_step.serialize_json(
            value["recovery_plan_execution_step"]
        )
    )
    return out


def deserialize_json(data: dict) -> RetryRecoveryPlanExecutionStepResponse:
    out: RetryRecoveryPlanExecutionStepResponse = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanExecutionStep") is not None:
        import capo_drs.types.recovery_plan_execution_step

        out["recovery_plan_execution_step"] = (
            capo_drs.types.recovery_plan_execution_step.deserialize_json(
                data["recoveryPlanExecutionStep"]
            )
        )
    else:
        raise DeserializationError(
            "RetryRecoveryPlanExecutionStepResponse.recovery_plan_execution_step required"
        )
    return out
