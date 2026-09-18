"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#EstimatedDiscounts``."""

from typing_extensions import NotRequired, TypedDict


class EstimatedDiscounts(TypedDict, closed=True):
    savings_plans_discount: NotRequired["float"]
    """<p>Estimated Savings Plans discounts.</p>"""
    reserved_instances_discount: NotRequired["float"]
    """<p>Estimated reserved instance discounts.</p>"""
    other_discount: NotRequired["float"]
    """<p>Estimated other discounts include all discounts that are not itemized. Itemized discounts include <code>reservedInstanceDiscount</code> and <code>savingsPlansDiscount</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EstimatedDiscounts) -> dict:
    out: dict = {}
    if "savings_plans_discount" in value:
        out["savingsPlansDiscount"] = (
            "NaN"
            if value["savings_plans_discount"] != value["savings_plans_discount"]
            else "Infinity"
            if value["savings_plans_discount"] == float("inf")
            else "-Infinity"
            if value["savings_plans_discount"] == float("-inf")
            else value["savings_plans_discount"]
        )
    if "reserved_instances_discount" in value:
        out["reservedInstancesDiscount"] = (
            "NaN"
            if value["reserved_instances_discount"]
            != value["reserved_instances_discount"]
            else "Infinity"
            if value["reserved_instances_discount"] == float("inf")
            else "-Infinity"
            if value["reserved_instances_discount"] == float("-inf")
            else value["reserved_instances_discount"]
        )
    if "other_discount" in value:
        out["otherDiscount"] = (
            "NaN"
            if value["other_discount"] != value["other_discount"]
            else "Infinity"
            if value["other_discount"] == float("inf")
            else "-Infinity"
            if value["other_discount"] == float("-inf")
            else value["other_discount"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EstimatedDiscounts:
    out: EstimatedDiscounts = {}  # type: ignore[typeddict-item]
    if data.get("savingsPlansDiscount") is not None:
        out["savings_plans_discount"] = float(data["savingsPlansDiscount"])
    if data.get("reservedInstancesDiscount") is not None:
        out["reserved_instances_discount"] = float(data["reservedInstancesDiscount"])
    if data.get("otherDiscount") is not None:
        out["other_discount"] = float(data["otherDiscount"])
    return out
