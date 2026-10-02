"""Generated from Smithy shape ``com.amazonaws.securityagent#ThreatModelJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.threat_model_job_summary

ThreatModelJobSummaryList: TypeAlias = list[
    "capo_securityagent.types.threat_model_job_summary.ThreatModelJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatModelJobSummaryList) -> list:
    import capo_securityagent.types.threat_model_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_securityagent.types.threat_model_job_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ThreatModelJobSummaryList:
    import capo_securityagent.types.threat_model_job_summary

    out: ThreatModelJobSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityagent.types.threat_model_job_summary.deserialize_json(item)
        )
    return out
