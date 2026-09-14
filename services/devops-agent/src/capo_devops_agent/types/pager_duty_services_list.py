"""Generated from Smithy shape ``com.amazonaws.devopsagent#PagerDutyServicesList``."""

from typing import TypeAlias

PagerDutyServicesList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: PagerDutyServicesList) -> list:
    return list(value)


def deserialize_json(data: list) -> PagerDutyServicesList:
    return [item for item in data if item is not None]
