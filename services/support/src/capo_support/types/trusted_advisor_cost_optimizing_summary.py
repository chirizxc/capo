"""Generated from Smithy shape ``com.amazonaws.support#TrustedAdvisorCostOptimizingSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_support.types.double


class TrustedAdvisorCostOptimizingSummary(TypedDict, closed=True):
    estimated_monthly_savings: "capo_support.types.double.Double"
    """<p>The estimated monthly savings that might be realized if the recommended operations are taken.</p>"""
    estimated_percent_monthly_savings: "capo_support.types.double.Double"
    """<p>The estimated percentage of savings that might be realized if the recommended operations are taken.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedAdvisorCostOptimizingSummary) -> dict:
    out: dict = {}
    out["estimatedMonthlySavings"] = (
        "NaN"
        if value.get("estimated_monthly_savings", 0)
        != value.get("estimated_monthly_savings", 0)
        else "Infinity"
        if value.get("estimated_monthly_savings", 0) == float("inf")
        else "-Infinity"
        if value.get("estimated_monthly_savings", 0) == float("-inf")
        else value.get("estimated_monthly_savings", 0)
    )
    out["estimatedPercentMonthlySavings"] = (
        "NaN"
        if value.get("estimated_percent_monthly_savings", 0)
        != value.get("estimated_percent_monthly_savings", 0)
        else "Infinity"
        if value.get("estimated_percent_monthly_savings", 0) == float("inf")
        else "-Infinity"
        if value.get("estimated_percent_monthly_savings", 0) == float("-inf")
        else value.get("estimated_percent_monthly_savings", 0)
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrustedAdvisorCostOptimizingSummary:
    out: TrustedAdvisorCostOptimizingSummary = {}  # type: ignore[typeddict-item]
    if data.get("estimatedMonthlySavings") is not None:
        out["estimated_monthly_savings"] = float(data["estimatedMonthlySavings"])
    else:
        out["estimated_monthly_savings"] = 0
    if data.get("estimatedPercentMonthlySavings") is not None:
        out["estimated_percent_monthly_savings"] = float(
            data["estimatedPercentMonthlySavings"]
        )
    else:
        out["estimated_percent_monthly_savings"] = 0
    return out
