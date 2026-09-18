"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#InstanceIdsList``."""

from typing import TypeAlias

InstanceIdsList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceIdsList) -> list:
    return list(value)


def deserialize_json(data: list) -> InstanceIdsList:
    return [item for item in data if item is not None]
