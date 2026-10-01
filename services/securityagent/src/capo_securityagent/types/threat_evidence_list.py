"""Generated from Smithy shape ``com.amazonaws.securityagent#ThreatEvidenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.threat_evidence_shape

ThreatEvidenceList: TypeAlias = list[
    "capo_securityagent.types.threat_evidence_shape.ThreatEvidenceShape"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatEvidenceList) -> list:
    import capo_securityagent.types.threat_evidence_shape

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.threat_evidence_shape.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThreatEvidenceList:
    import capo_securityagent.types.threat_evidence_shape

    out: ThreatEvidenceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityagent.types.threat_evidence_shape.deserialize_json(item)
        )
    return out
