"""Generated from Smithy shape ``com.amazonaws.securityagent#ThreatModelSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.threat_model_summary

ThreatModelSummaryList: TypeAlias = list[
    "capo_securityagent.types.threat_model_summary.ThreatModelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatModelSummaryList) -> list:
    import capo_securityagent.types.threat_model_summary

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.threat_model_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThreatModelSummaryList:
    import capo_securityagent.types.threat_model_summary

    out: ThreatModelSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityagent.types.threat_model_summary.deserialize_json(item))
    return out
