"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryPlanServers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.recovery_plan_server

RecoveryPlanServers: TypeAlias = list[
    "capo_drs.types.recovery_plan_server.RecoveryPlanServer"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPlanServers) -> list:
    import capo_drs.types.recovery_plan_server

    out: list = []
    for item in value:
        out.append(capo_drs.types.recovery_plan_server.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecoveryPlanServers:
    import capo_drs.types.recovery_plan_server

    out: RecoveryPlanServers = []
    for item in data:
        if item is None:
            continue
        out.append(capo_drs.types.recovery_plan_server.deserialize_json(item))
    return out
