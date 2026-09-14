"""Generated from Smithy shape ``com.amazonaws.inspector2#Usage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.currency
    import capo_inspector2.types.monthly_cost_estimate
    import capo_inspector2.types.usage_type
    import capo_inspector2.types.usage_value


class Usage(TypedDict, closed=True):
    type: NotRequired["capo_inspector2.types.usage_type.UsageType"]
    """<p>The type scan.</p>"""
    total: "capo_inspector2.types.usage_value.UsageValue"
    """<p>The total of usage.</p>"""
    estimated_monthly_cost: (
        "capo_inspector2.types.monthly_cost_estimate.MonthlyCostEstimate"
    )
    """<p>The estimated monthly cost of Amazon Inspector.</p>"""
    currency: NotRequired["capo_inspector2.types.currency.Currency"]
    """<p>The currency type used when calculating usage data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Usage) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    out["total"] = (
        "NaN"
        if value.get("total", 0) != value.get("total", 0)
        else "Infinity"
        if value.get("total", 0) == float("inf")
        else "-Infinity"
        if value.get("total", 0) == float("-inf")
        else value.get("total", 0)
    )
    out["estimatedMonthlyCost"] = (
        "NaN"
        if value.get("estimated_monthly_cost", 0)
        != value.get("estimated_monthly_cost", 0)
        else "Infinity"
        if value.get("estimated_monthly_cost", 0) == float("inf")
        else "-Infinity"
        if value.get("estimated_monthly_cost", 0) == float("-inf")
        else value.get("estimated_monthly_cost", 0)
    )
    if "currency" in value:
        out["currency"] = value["currency"]
    return out


def deserialize_json(data: dict) -> Usage:
    out: Usage = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("total") is not None:
        out["total"] = float(data["total"])
    else:
        out["total"] = 0
    if data.get("estimatedMonthlyCost") is not None:
        out["estimated_monthly_cost"] = float(data["estimatedMonthlyCost"])
    else:
        out["estimated_monthly_cost"] = 0
    if data.get("currency") is not None:
        out["currency"] = data["currency"]
    return out
