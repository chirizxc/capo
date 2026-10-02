"""Generated from Smithy shape ``com.amazonaws.securityagent#ThreatModelIdList``."""

from typing import TypeAlias

ThreatModelIdList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatModelIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ThreatModelIdList:
    return [item for item in data if item is not None]
