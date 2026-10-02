"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DependencyInsightsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.dependency_insight

DependencyInsightsList: TypeAlias = list[
    "capo_resiliencehubv2.types.dependency_insight.DependencyInsight"
]


# --- restJson1 ser/de ---
def serialize_json(value: DependencyInsightsList) -> list:
    import capo_resiliencehubv2.types.dependency_insight

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.dependency_insight.serialize_json(item))
    return out


def deserialize_json(data: list) -> DependencyInsightsList:
    import capo_resiliencehubv2.types.dependency_insight

    out: DependencyInsightsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_resiliencehubv2.types.dependency_insight.deserialize_json(item))
    return out
