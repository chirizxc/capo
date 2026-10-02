"""Generated from Smithy shape ``com.amazonaws.securityagent#TaskExecutionStatusFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.task_execution_status

TaskExecutionStatusFilterList: TypeAlias = list[
    "capo_securityagent.types.task_execution_status.TaskExecutionStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskExecutionStatusFilterList) -> list:
    import capo_securityagent.types.task_execution_status

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.task_execution_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> TaskExecutionStatusFilterList:
    import capo_securityagent.types.task_execution_status

    out: TaskExecutionStatusFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityagent.types.task_execution_status.deserialize_json(item)
        )
    return out
