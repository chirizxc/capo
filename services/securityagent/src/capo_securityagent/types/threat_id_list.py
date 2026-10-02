"""Generated from Smithy shape ``com.amazonaws.securityagent#ThreatIdList``."""

from typing import TypeAlias

ThreatIdList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ThreatIdList:
    return [item for item in data if item is not None]
