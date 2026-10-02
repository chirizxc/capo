"""Generated from Smithy shape ``com.amazonaws.securityagent#RiskLevelFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.risk_level

RiskLevelFilterList: TypeAlias = list["capo_securityagent.types.risk_level.RiskLevel"]


# --- restJson1 ser/de ---
def serialize_json(value: RiskLevelFilterList) -> list:
    import capo_securityagent.types.risk_level

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.risk_level.serialize_json(item))
    return out


def deserialize_json(data: list) -> RiskLevelFilterList:
    import capo_securityagent.types.risk_level

    out: RiskLevelFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityagent.types.risk_level.deserialize_json(item))
    return out
