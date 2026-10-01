"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#ListRecommendationsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_trustedadvisor.types.aws_resource_arn
    import capo_trustedadvisor.types.check_arn
    import capo_trustedadvisor.types.recommendation_language
    import capo_trustedadvisor.types.recommendation_pillar
    import capo_trustedadvisor.types.resource_status


class ListRecommendationsForResourceRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return per page</p>"""
    aws_resource_arn: "capo_trustedadvisor.types.aws_resource_arn.AwsResourceArn"
    """<p>The ARN of the AWS resource to query recommendations for</p>"""
    pillar: NotRequired[
        "capo_trustedadvisor.types.recommendation_pillar.RecommendationPillar"
    ]
    """<p>The pillar that the recommendation belongs to</p>"""
    status: NotRequired["capo_trustedadvisor.types.resource_status.ResourceStatus"]
    """<p>The current status of the Recommendation Resource</p>"""
    check_arn: NotRequired["capo_trustedadvisor.types.check_arn.CheckArn"]
    """<p>The AWS Trusted Advisor Check ARN that relates to the Recommendation</p>"""
    language: NotRequired[
        "capo_trustedadvisor.types.recommendation_language.RecommendationLanguage"
    ]
    """<p>The ISO 639-1 code for the language that you want your recommendations to appear in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRecommendationsForResourceRequest:
    out: ListRecommendationsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
