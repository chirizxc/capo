"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ProspectingInsights``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_score_level


class ProspectingInsights(TypedDict, closed=True):
    marketplace_engagement_score: NotRequired[
        "capo_partnercentral_selling.types.engagement_score_level.EngagementScoreLevel"
    ]
    """<p>A score that indicates the prospected customer's level of engagement with AWS Marketplace. Valid values are <code>High</code>, <code>Medium</code>, and <code>Low</code>.</p>"""
    solution_score: NotRequired["str"]
    """<p>A score that indicates how well the partner's solution fits the prospected customer's needs.</p>"""
    solution_category: NotRequired["str"]
    """<p>The primary solution category classification for the prospected customer. This indicates the type of solution that best addresses their needs.</p>"""
    solution_sub_category: NotRequired["str"]
    """<p>The solution sub-category classification for the prospected customer. This provides more granular categorization of the recommended solution type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProspectingInsights) -> dict:
    out: dict = {}
    if "marketplace_engagement_score" in value:
        out["MarketplaceEngagementScore"] = value["marketplace_engagement_score"]
    if "solution_score" in value:
        out["SolutionScore"] = value["solution_score"]
    if "solution_category" in value:
        out["SolutionCategory"] = value["solution_category"]
    if "solution_sub_category" in value:
        out["SolutionSubCategory"] = value["solution_sub_category"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ProspectingInsights:
    out: ProspectingInsights = {}  # type: ignore[typeddict-item]
    if data.get("MarketplaceEngagementScore") is not None:
        out["marketplace_engagement_score"] = data["MarketplaceEngagementScore"]
    if data.get("SolutionScore") is not None:
        out["solution_score"] = data["SolutionScore"]
    if data.get("SolutionCategory") is not None:
        out["solution_category"] = data["SolutionCategory"]
    if data.get("SolutionSubCategory") is not None:
        out["solution_sub_category"] = data["SolutionSubCategory"]
    return out
