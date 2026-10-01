"""Generated from Smithy shape ``com.amazonaws.securityagent#ThreatModelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.threat_model

ThreatModelList: TypeAlias = list["capo_securityagent.types.threat_model.ThreatModel"]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatModelList) -> list:
    import capo_securityagent.types.threat_model

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.threat_model.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThreatModelList:
    import capo_securityagent.types.threat_model

    out: ThreatModelList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityagent.types.threat_model.deserialize_json(item))
    return out
