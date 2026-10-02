"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#LeadInsights``."""

from typing_extensions import NotRequired, TypedDict


class LeadInsights(TypedDict, closed=True):
    lead_readiness_score: NotRequired["str"]
    """<p>A score that indicates the lead's readiness for engagement. Valid values are <code>Low</code>, <code>Medium</code>, and <code>High</code>. Use this score to prioritize leads based on their likelihood of conversion.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LeadInsights) -> dict:
    out: dict = {}
    if "lead_readiness_score" in value:
        out["LeadReadinessScore"] = value["lead_readiness_score"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LeadInsights:
    out: LeadInsights = {}  # type: ignore[typeddict-item]
    if data.get("LeadReadinessScore") is not None:
        out["lead_readiness_score"] = data["LeadReadinessScore"]
    return out
