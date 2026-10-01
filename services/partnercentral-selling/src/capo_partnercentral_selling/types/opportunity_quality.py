"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#OpportunityQuality``."""

from typing_extensions import NotRequired, TypedDict


class OpportunityQuality(TypedDict, closed=True):
    score: NotRequired["int"]
    """<p>Deal quality score based on opportunity content completeness and sales methodology criteria. Values range from 0 to 100.</p>"""
    trend: NotRequired["str"]
    """<p>Direction of score change since last scoring iteration. Known values: <code>Improving</code>, <code>Declining</code>, <code>No Change</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpportunityQuality) -> dict:
    out: dict = {}
    if "score" in value:
        out["Score"] = value["score"]
    if "trend" in value:
        out["Trend"] = value["trend"]
    return out


def deserialize_aws_json_1_0(data: dict) -> OpportunityQuality:
    out: OpportunityQuality = {}  # type: ignore[typeddict-item]
    if data.get("Score") is not None:
        out["score"] = data["Score"]
    if data.get("Trend") is not None:
        out["trend"] = data["Trend"]
    return out
