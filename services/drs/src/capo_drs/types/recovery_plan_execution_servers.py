"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryPlanExecutionServers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.recovery_plan_execution_server

RecoveryPlanExecutionServers: TypeAlias = list[
    "capo_drs.types.recovery_plan_execution_server.RecoveryPlanExecutionServer"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPlanExecutionServers) -> list:
    import capo_drs.types.recovery_plan_execution_server

    out: list = []
    for item in value:
        out.append(capo_drs.types.recovery_plan_execution_server.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecoveryPlanExecutionServers:
    import capo_drs.types.recovery_plan_execution_server

    out: RecoveryPlanExecutionServers = []
    for item in data:
        if item is None:
            continue
        out.append(capo_drs.types.recovery_plan_execution_server.deserialize_json(item))
    return out
