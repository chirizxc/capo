"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#RecommendationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.recommendation

RecommendationList: TypeAlias = list[
    "capo_partnercentral_selling.types.recommendation.Recommendation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationList) -> list:
    import capo_partnercentral_selling.types.recommendation

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.recommendation.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RecommendationList:
    import capo_partnercentral_selling.types.recommendation

    out: RecommendationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_selling.types.recommendation.deserialize_aws_json_1_0(
                item
            )
        )
    return out
