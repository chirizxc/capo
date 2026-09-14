"""Generated from Smithy shape ``com.amazonaws.devopsagent#NewRelicAlertPolicyIds``."""

from typing import TypeAlias

NewRelicAlertPolicyIds: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: NewRelicAlertPolicyIds) -> list:
    return list(value)


def deserialize_json(data: list) -> NewRelicAlertPolicyIds:
    return [item for item in data if item is not None]
