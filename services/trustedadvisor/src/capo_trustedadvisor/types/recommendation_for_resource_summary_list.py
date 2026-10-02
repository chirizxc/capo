"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationForResourceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_trustedadvisor.types.recommendation_for_resource_summary

RecommendationForResourceSummaryList: TypeAlias = list[
    "capo_trustedadvisor.types.recommendation_for_resource_summary.RecommendationForResourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationForResourceSummaryList) -> list:
    import capo_trustedadvisor.types.recommendation_for_resource_summary

    out: list = []
    for item in value:
        out.append(
            capo_trustedadvisor.types.recommendation_for_resource_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RecommendationForResourceSummaryList:
    import capo_trustedadvisor.types.recommendation_for_resource_summary

    out: RecommendationForResourceSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_trustedadvisor.types.recommendation_for_resource_summary.deserialize_json(
                item
            )
        )
    return out
