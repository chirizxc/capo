"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ResourcePricing``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.estimated_discounts


class ResourcePricing(TypedDict, closed=True):
    estimated_cost_before_discounts: NotRequired["float"]
    """<p>The savings estimate using Amazon Web Services public pricing without incorporating any discounts.</p>"""
    estimated_net_unused_amortized_commitments: NotRequired["float"]
    """<p>The estimated net unused amortized commitment for the recommendation.</p>"""
    estimated_discounts: NotRequired[
        "capo_cost_optimization_hub.types.estimated_discounts.EstimatedDiscounts"
    ]
    """<p>The estimated discounts for a recommendation.</p>"""
    estimated_cost_after_discounts: NotRequired["float"]
    """<p>The savings estimate incorporating all discounts with Amazon Web Services, such as Reserved Instances and Savings Plans.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourcePricing) -> dict:
    out: dict = {}
    if "estimated_cost_before_discounts" in value:
        out["estimatedCostBeforeDiscounts"] = (
            "NaN"
            if value["estimated_cost_before_discounts"]
            != value["estimated_cost_before_discounts"]
            else "Infinity"
            if value["estimated_cost_before_discounts"] == float("inf")
            else "-Infinity"
            if value["estimated_cost_before_discounts"] == float("-inf")
            else value["estimated_cost_before_discounts"]
        )
    if "estimated_net_unused_amortized_commitments" in value:
        out["estimatedNetUnusedAmortizedCommitments"] = (
            "NaN"
            if value["estimated_net_unused_amortized_commitments"]
            != value["estimated_net_unused_amortized_commitments"]
            else "Infinity"
            if value["estimated_net_unused_amortized_commitments"] == float("inf")
            else "-Infinity"
            if value["estimated_net_unused_amortized_commitments"] == float("-inf")
            else value["estimated_net_unused_amortized_commitments"]
        )
    if "estimated_discounts" in value:
        import capo_cost_optimization_hub.types.estimated_discounts

        out["estimatedDiscounts"] = (
            capo_cost_optimization_hub.types.estimated_discounts.serialize_aws_json_1_0(
                value["estimated_discounts"]
            )
        )
    if "estimated_cost_after_discounts" in value:
        out["estimatedCostAfterDiscounts"] = (
            "NaN"
            if value["estimated_cost_after_discounts"]
            != value["estimated_cost_after_discounts"]
            else "Infinity"
            if value["estimated_cost_after_discounts"] == float("inf")
            else "-Infinity"
            if value["estimated_cost_after_discounts"] == float("-inf")
            else value["estimated_cost_after_discounts"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourcePricing:
    out: ResourcePricing = {}  # type: ignore[typeddict-item]
    if data.get("estimatedCostBeforeDiscounts") is not None:
        out["estimated_cost_before_discounts"] = float(
            data["estimatedCostBeforeDiscounts"]
        )
    if data.get("estimatedNetUnusedAmortizedCommitments") is not None:
        out["estimated_net_unused_amortized_commitments"] = float(
            data["estimatedNetUnusedAmortizedCommitments"]
        )
    if data.get("estimatedDiscounts") is not None:
        import capo_cost_optimization_hub.types.estimated_discounts

        out["estimated_discounts"] = (
            capo_cost_optimization_hub.types.estimated_discounts.deserialize_aws_json_1_0(
                data["estimatedDiscounts"]
            )
        )
    if data.get("estimatedCostAfterDiscounts") is not None:
        out["estimated_cost_after_discounts"] = float(
            data["estimatedCostAfterDiscounts"]
        )
    return out
