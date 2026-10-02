"""Generated from Smithy shape ``com.amazonaws.wellarchitected#RecommendedFixSteps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.recommended_fix_step

RecommendedFixSteps: TypeAlias = list[
    "capo_wellarchitected.types.recommended_fix_step.RecommendedFixStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendedFixSteps) -> list:
    return list(value)


def deserialize_json(data: list) -> RecommendedFixSteps:
    return [item for item in data if item is not None]
