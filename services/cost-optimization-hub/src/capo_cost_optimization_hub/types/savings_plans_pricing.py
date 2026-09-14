"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#SavingsPlansPricing``."""

from typing_extensions import NotRequired, TypedDict


class SavingsPlansPricing(TypedDict, closed=True):
    monthly_savings_plans_eligible_cost: NotRequired["float"]
    """<p>The cost of paying for the recommended Savings Plans monthly.</p>"""
    estimated_monthly_commitment: NotRequired["float"]
    """<p>Estimated monthly commitment for the Savings Plans.</p>"""
    savings_percentage: NotRequired["float"]
    """<p>Estimated savings as a percentage of your overall costs after buying the Savings Plans.</p>"""
    estimated_on_demand_cost: NotRequired["float"]
    """<p>Estimated On-Demand cost you will pay after buying the Savings Plans.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SavingsPlansPricing) -> dict:
    out: dict = {}
    if "monthly_savings_plans_eligible_cost" in value:
        out["monthlySavingsPlansEligibleCost"] = (
            "NaN"
            if value["monthly_savings_plans_eligible_cost"]
            != value["monthly_savings_plans_eligible_cost"]
            else "Infinity"
            if value["monthly_savings_plans_eligible_cost"] == float("inf")
            else "-Infinity"
            if value["monthly_savings_plans_eligible_cost"] == float("-inf")
            else value["monthly_savings_plans_eligible_cost"]
        )
    if "estimated_monthly_commitment" in value:
        out["estimatedMonthlyCommitment"] = (
            "NaN"
            if value["estimated_monthly_commitment"]
            != value["estimated_monthly_commitment"]
            else "Infinity"
            if value["estimated_monthly_commitment"] == float("inf")
            else "-Infinity"
            if value["estimated_monthly_commitment"] == float("-inf")
            else value["estimated_monthly_commitment"]
        )
    if "savings_percentage" in value:
        out["savingsPercentage"] = (
            "NaN"
            if value["savings_percentage"] != value["savings_percentage"]
            else "Infinity"
            if value["savings_percentage"] == float("inf")
            else "-Infinity"
            if value["savings_percentage"] == float("-inf")
            else value["savings_percentage"]
        )
    if "estimated_on_demand_cost" in value:
        out["estimatedOnDemandCost"] = (
            "NaN"
            if value["estimated_on_demand_cost"] != value["estimated_on_demand_cost"]
            else "Infinity"
            if value["estimated_on_demand_cost"] == float("inf")
            else "-Infinity"
            if value["estimated_on_demand_cost"] == float("-inf")
            else value["estimated_on_demand_cost"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SavingsPlansPricing:
    out: SavingsPlansPricing = {}  # type: ignore[typeddict-item]
    if data.get("monthlySavingsPlansEligibleCost") is not None:
        out["monthly_savings_plans_eligible_cost"] = float(
            data["monthlySavingsPlansEligibleCost"]
        )
    if data.get("estimatedMonthlyCommitment") is not None:
        out["estimated_monthly_commitment"] = float(data["estimatedMonthlyCommitment"])
    if data.get("savingsPercentage") is not None:
        out["savings_percentage"] = float(data["savingsPercentage"])
    if data.get("estimatedOnDemandCost") is not None:
        out["estimated_on_demand_cost"] = float(data["estimatedOnDemandCost"])
    return out
