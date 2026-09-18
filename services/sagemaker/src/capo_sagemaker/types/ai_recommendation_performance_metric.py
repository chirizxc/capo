"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationPerformanceMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.string


class AIRecommendationPerformanceMetric(TypedDict, closed=True):
    metric: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The name of the performance metric.</p>"""
    stat: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The statistical measure for the metric.</p>"""
    value: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The value of the metric.</p>"""
    unit: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The unit of the metric value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationPerformanceMetric) -> dict:
    out: dict = {}
    if "metric" in value:
        out["Metric"] = value["metric"]
    if "stat" in value:
        out["Stat"] = value["stat"]
    if "value" in value:
        out["Value"] = value["value"]
    if "unit" in value:
        out["Unit"] = value["unit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AIRecommendationPerformanceMetric:
    out: AIRecommendationPerformanceMetric = {}  # type: ignore[typeddict-item]
    if data.get("Metric") is not None:
        out["metric"] = data["Metric"]
    if data.get("Stat") is not None:
        out["stat"] = data["Stat"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Unit") is not None:
        out["unit"] = data["Unit"]
    return out
