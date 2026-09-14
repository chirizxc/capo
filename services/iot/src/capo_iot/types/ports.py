"""Generated from Smithy shape ``com.amazonaws.iot#Ports``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.port

Ports: TypeAlias = list["capo_iot.types.port.Port"]


# --- restJson1 ser/de ---
def serialize_json(value: Ports) -> list:
    return list(value)


def deserialize_json(data: list) -> Ports:
    return [item for item in data if item is not None]
