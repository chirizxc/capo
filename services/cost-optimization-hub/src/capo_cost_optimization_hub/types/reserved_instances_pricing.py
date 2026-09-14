"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ReservedInstancesPricing``."""

from typing_extensions import NotRequired, TypedDict


class ReservedInstancesPricing(TypedDict, closed=True):
    estimated_on_demand_cost: NotRequired["float"]
    """<p>The remaining On-Demand cost estimated to not be covered by the recommended reserved instance, over the length of the lookback period.</p>"""
    monthly_reservation_eligible_cost: NotRequired["float"]
    """<p>The cost of paying for the recommended reserved instance monthly.</p>"""
    savings_percentage: NotRequired["float"]
    """<p>The savings percentage relative to the total On-Demand costs that are associated with this instance.</p>"""
    estimated_monthly_amortized_reservation_cost: NotRequired["float"]
    """<p>The estimated cost of your recurring monthly fees for the recommended reserved instance across the month.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReservedInstancesPricing) -> dict:
    out: dict = {}
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
    if "monthly_reservation_eligible_cost" in value:
        out["monthlyReservationEligibleCost"] = (
            "NaN"
            if value["monthly_reservation_eligible_cost"]
            != value["monthly_reservation_eligible_cost"]
            else "Infinity"
            if value["monthly_reservation_eligible_cost"] == float("inf")
            else "-Infinity"
            if value["monthly_reservation_eligible_cost"] == float("-inf")
            else value["monthly_reservation_eligible_cost"]
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
    if "estimated_monthly_amortized_reservation_cost" in value:
        out["estimatedMonthlyAmortizedReservationCost"] = (
            "NaN"
            if value["estimated_monthly_amortized_reservation_cost"]
            != value["estimated_monthly_amortized_reservation_cost"]
            else "Infinity"
            if value["estimated_monthly_amortized_reservation_cost"] == float("inf")
            else "-Infinity"
            if value["estimated_monthly_amortized_reservation_cost"] == float("-inf")
            else value["estimated_monthly_amortized_reservation_cost"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReservedInstancesPricing:
    out: ReservedInstancesPricing = {}  # type: ignore[typeddict-item]
    if data.get("estimatedOnDemandCost") is not None:
        out["estimated_on_demand_cost"] = float(data["estimatedOnDemandCost"])
    if data.get("monthlyReservationEligibleCost") is not None:
        out["monthly_reservation_eligible_cost"] = float(
            data["monthlyReservationEligibleCost"]
        )
    if data.get("savingsPercentage") is not None:
        out["savings_percentage"] = float(data["savingsPercentage"])
    if data.get("estimatedMonthlyAmortizedReservationCost") is not None:
        out["estimated_monthly_amortized_reservation_cost"] = float(
            data["estimatedMonthlyAmortizedReservationCost"]
        )
    return out
