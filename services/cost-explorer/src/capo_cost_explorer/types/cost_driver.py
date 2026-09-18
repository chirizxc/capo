"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostDriver``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.comparison_metrics
    import capo_cost_explorer.types.generic_string


class CostDriver(TypedDict, closed=True):
    type: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The category or classification of the cost driver.</p> <p>Values include: BUNDLED_DISCOUNT, CREDIT, OUT_OF_CYCLE_CHARGE, REFUND, RECURRING_RESERVATION_FEE, RESERVATION_USAGE, RI_VOLUME_DISCOUNT, SAVINGS_PLAN_USAGE, SAVINGS_PLAN_RECURRING_FEE, SUPPORT_FEE, TAX, UPFRONT_RESERVATION_FEE, USAGE_CHANGE, COMMITMENT</p>"""
    name: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The specific identifier of the cost driver.</p>"""
    metrics: NotRequired[
        "capo_cost_explorer.types.comparison_metrics.ComparisonMetrics"
    ]
    """<p>A mapping of metric names to their comparison values, measuring the impact of this cost driver.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostDriver) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "name" in value:
        out["Name"] = value["name"]
    if "metrics" in value:
        import capo_cost_explorer.types.comparison_metrics

        out["Metrics"] = (
            capo_cost_explorer.types.comparison_metrics.serialize_aws_json_1_1(
                value["metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CostDriver:
    out: CostDriver = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Metrics") is not None:
        import capo_cost_explorer.types.comparison_metrics

        out["metrics"] = (
            capo_cost_explorer.types.comparison_metrics.deserialize_aws_json_1_1(
                data["Metrics"]
            )
        )
    return out
