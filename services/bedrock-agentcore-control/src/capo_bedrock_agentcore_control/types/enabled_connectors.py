"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EnabledConnectors``."""

from typing import TypeAlias

EnabledConnectors: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: EnabledConnectors) -> list:
    return list(value)


def deserialize_json(data: list) -> EnabledConnectors:
    return [item for item in data if item is not None]
