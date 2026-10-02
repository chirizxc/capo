"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ImpactDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.impact_detail

ImpactDetails: TypeAlias = list["capo_wellarchitected.types.impact_detail.ImpactDetail"]


# --- restJson1 ser/de ---
def serialize_json(value: ImpactDetails) -> list:
    return list(value)


def deserialize_json(data: list) -> ImpactDetails:
    return [item for item in data if item is not None]
