"""Generated from Smithy shape ``com.amazonaws.securityagent#ThreatModelJobTaskSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.threat_model_job_task_summary

ThreatModelJobTaskSummaryList: TypeAlias = list[
    "capo_securityagent.types.threat_model_job_task_summary.ThreatModelJobTaskSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatModelJobTaskSummaryList) -> list:
    import capo_securityagent.types.threat_model_job_task_summary

    out: list = []
    for item in value:
        out.append(
            capo_securityagent.types.threat_model_job_task_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ThreatModelJobTaskSummaryList:
    import capo_securityagent.types.threat_model_job_task_summary

    out: ThreatModelJobTaskSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityagent.types.threat_model_job_task_summary.deserialize_json(
                item
            )
        )
    return out
