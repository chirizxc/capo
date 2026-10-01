"""Generated from Smithy shape ``com.amazonaws.wellarchitected#RecommendationTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.recommendation_type

RecommendationTypes: TypeAlias = list[
    "capo_wellarchitected.types.recommendation_type.RecommendationType"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationTypes) -> list:
    import capo_wellarchitected.types.recommendation_type

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.recommendation_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecommendationTypes:
    import capo_wellarchitected.types.recommendation_type

    out: RecommendationTypes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wellarchitected.types.recommendation_type.deserialize_json(item)
        )
    return out
