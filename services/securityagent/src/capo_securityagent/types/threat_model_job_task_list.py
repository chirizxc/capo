"""Generated from Smithy shape ``com.amazonaws.securityagent#ThreatModelJobTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.threat_model_job_task

ThreatModelJobTaskList: TypeAlias = list[
    "capo_securityagent.types.threat_model_job_task.ThreatModelJobTask"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatModelJobTaskList) -> list:
    import capo_securityagent.types.threat_model_job_task

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.threat_model_job_task.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThreatModelJobTaskList:
    import capo_securityagent.types.threat_model_job_task

    out: ThreatModelJobTaskList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityagent.types.threat_model_job_task.deserialize_json(item)
        )
    return out
