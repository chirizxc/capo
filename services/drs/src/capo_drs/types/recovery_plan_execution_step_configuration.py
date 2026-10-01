"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryPlanExecutionStepConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_drs.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_drs.types.execution_server_step_configuration
    import capo_drs.types.wait_step_configuration


class _RecoveryPlanExecutionStepConfiguration_executionServerStepConfiguration(
    TypedDict, closed=True
):
    executionServerStepConfiguration: "capo_drs.types.execution_server_step_configuration.ExecutionServerStepConfiguration"


class _RecoveryPlanExecutionStepConfiguration_waitStepConfiguration(
    TypedDict, closed=True
):
    waitStepConfiguration: (
        "capo_drs.types.wait_step_configuration.WaitStepConfiguration"
    )


RecoveryPlanExecutionStepConfiguration: TypeAlias = (
    _RecoveryPlanExecutionStepConfiguration_executionServerStepConfiguration
    | _RecoveryPlanExecutionStepConfiguration_waitStepConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPlanExecutionStepConfiguration) -> dict:
    if "executionServerStepConfiguration" in value:
        import capo_drs.types.execution_server_step_configuration

        return {
            "executionServerStepConfiguration": capo_drs.types.execution_server_step_configuration.serialize_json(
                value["executionServerStepConfiguration"]
            )
        }
    elif "waitStepConfiguration" in value:
        import capo_drs.types.wait_step_configuration

        return {
            "waitStepConfiguration": capo_drs.types.wait_step_configuration.serialize_json(
                value["waitStepConfiguration"]
            )
        }
    else:
        raise SerializationError(
            "RecoveryPlanExecutionStepConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> RecoveryPlanExecutionStepConfiguration:
    if data.get("executionServerStepConfiguration") is not None:
        import capo_drs.types.execution_server_step_configuration

        return {
            "executionServerStepConfiguration": capo_drs.types.execution_server_step_configuration.deserialize_json(
                data["executionServerStepConfiguration"]
            )
        }
    elif data.get("waitStepConfiguration") is not None:
        import capo_drs.types.wait_step_configuration

        return {
            "waitStepConfiguration": capo_drs.types.wait_step_configuration.deserialize_json(
                data["waitStepConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "RecoveryPlanExecutionStepConfiguration: no recognized variant key"
        )
