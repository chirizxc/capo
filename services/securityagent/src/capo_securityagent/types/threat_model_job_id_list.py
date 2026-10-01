"""Generated from Smithy shape ``com.amazonaws.securityagent#ThreatModelJobIdList``."""

from typing import TypeAlias

ThreatModelJobIdList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatModelJobIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ThreatModelJobIdList:
    return [item for item in data if item is not None]
