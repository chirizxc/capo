"""Generated from Smithy shape ``com.amazonaws.securityagent#ThreatModelJobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.threat_model_job

ThreatModelJobList: TypeAlias = list[
    "capo_securityagent.types.threat_model_job.ThreatModelJob"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatModelJobList) -> list:
    import capo_securityagent.types.threat_model_job

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.threat_model_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThreatModelJobList:
    import capo_securityagent.types.threat_model_job

    out: ThreatModelJobList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityagent.types.threat_model_job.deserialize_json(item))
    return out
