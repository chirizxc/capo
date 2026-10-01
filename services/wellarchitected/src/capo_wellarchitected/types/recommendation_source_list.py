"""Generated from Smithy shape ``com.amazonaws.wellarchitected#RecommendationSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.recommendation_source

RecommendationSourceList: TypeAlias = list[
    "capo_wellarchitected.types.recommendation_source.RecommendationSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationSourceList) -> list:
    import capo_wellarchitected.types.recommendation_source

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.recommendation_source.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RecommendationSourceList:
    import capo_wellarchitected.types.recommendation_source

    out: RecommendationSourceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wellarchitected.types.recommendation_source.deserialize_json(item)
        )
    return out
