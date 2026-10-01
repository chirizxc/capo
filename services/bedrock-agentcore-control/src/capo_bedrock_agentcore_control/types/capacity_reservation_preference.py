"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CapacityReservationPreference``."""

from typing import Literal, TypeAlias, cast

CapacityReservationPreference: TypeAlias = Literal[
    "capacity-reservations-only",
    "open",
    "none",
]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityReservationPreference) -> str:
    return value


def deserialize_json(data: str) -> CapacityReservationPreference:
    return cast(CapacityReservationPreference, data)
