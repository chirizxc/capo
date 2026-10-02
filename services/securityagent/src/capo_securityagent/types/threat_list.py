"""Generated from Smithy shape ``com.amazonaws.securityagent#ThreatList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.threat

ThreatList: TypeAlias = list["capo_securityagent.types.threat.Threat"]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatList) -> list:
    import capo_securityagent.types.threat

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.threat.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThreatList:
    import capo_securityagent.types.threat

    out: ThreatList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityagent.types.threat.deserialize_json(item))
    return out
