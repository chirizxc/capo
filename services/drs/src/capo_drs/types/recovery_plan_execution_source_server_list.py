"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryPlanExecutionSourceServerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.recovery_plan_execution_source_server

RecoveryPlanExecutionSourceServerList: TypeAlias = list[
    "capo_drs.types.recovery_plan_execution_source_server.RecoveryPlanExecutionSourceServer"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPlanExecutionSourceServerList) -> list:
    import capo_drs.types.recovery_plan_execution_source_server

    out: list = []
    for item in value:
        out.append(
            capo_drs.types.recovery_plan_execution_source_server.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RecoveryPlanExecutionSourceServerList:
    import capo_drs.types.recovery_plan_execution_source_server

    out: RecoveryPlanExecutionSourceServerList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_drs.types.recovery_plan_execution_source_server.deserialize_json(item)
        )
    return out
