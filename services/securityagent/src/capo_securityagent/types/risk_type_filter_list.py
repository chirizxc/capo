"""Generated from Smithy shape ``com.amazonaws.securityagent#RiskTypeFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.risk_type

RiskTypeFilterList: TypeAlias = list["capo_securityagent.types.risk_type.RiskType"]


# --- restJson1 ser/de ---
def serialize_json(value: RiskTypeFilterList) -> list:
    import capo_securityagent.types.risk_type

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.risk_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> RiskTypeFilterList:
    import capo_securityagent.types.risk_type

    out: RiskTypeFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityagent.types.risk_type.deserialize_json(item))
    return out
