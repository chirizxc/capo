"""Generated from Smithy shape ``com.amazonaws.guardduty#ObservationNumbers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.long

ObservationNumbers: TypeAlias = list["capo_guardduty.types.long.Long"]


# --- restJson1 ser/de ---
def serialize_json(value: ObservationNumbers) -> list:
    return list(value)


def deserialize_json(data: list) -> ObservationNumbers:
    return [item for item in data if item is not None]
