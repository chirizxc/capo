"""Generated from Smithy shape ``com.amazonaws.securityagent#ThreatSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.threat_summary

ThreatSummaryList: TypeAlias = list[
    "capo_securityagent.types.threat_summary.ThreatSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatSummaryList) -> list:
    import capo_securityagent.types.threat_summary

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.threat_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThreatSummaryList:
    import capo_securityagent.types.threat_summary

    out: ThreatSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityagent.types.threat_summary.deserialize_json(item))
    return out
