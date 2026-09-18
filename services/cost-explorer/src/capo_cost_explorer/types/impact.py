"""Generated from Smithy shape ``com.amazonaws.costexplorer#Impact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_double
    import capo_cost_explorer.types.nullable_non_negative_double


class Impact(TypedDict, closed=True):
    max_impact: "capo_cost_explorer.types.generic_double.GenericDouble"
    """<p>The maximum dollar value that's observed for an anomaly.</p>"""
    total_impact: "capo_cost_explorer.types.generic_double.GenericDouble"
    """<p>The cumulative dollar difference between the total actual spend and total expected spend. It is calculated as <code>TotalActualSpend - TotalExpectedSpend</code>.</p>"""
    total_actual_spend: NotRequired[
        "capo_cost_explorer.types.nullable_non_negative_double.NullableNonNegativeDouble"
    ]
    """<p>The cumulative dollar amount that was actually spent during the anomaly.</p>"""
    total_expected_spend: NotRequired[
        "capo_cost_explorer.types.nullable_non_negative_double.NullableNonNegativeDouble"
    ]
    """<p>The cumulative dollar amount that was expected to be spent during the anomaly. It is calculated using advanced machine learning models to determine the typical spending pattern based on historical data for a customer.</p>"""
    total_impact_percentage: NotRequired[
        "capo_cost_explorer.types.nullable_non_negative_double.NullableNonNegativeDouble"
    ]
    """<p>The cumulative percentage difference between the total actual spend and total expected spend. It is calculated as <code>(TotalImpact / TotalExpectedSpend) * 100</code>. When <code>TotalExpectedSpend</code> is zero, this field is omitted. Expected spend can be zero in situations such as when you start to use a service for the first time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Impact) -> dict:
    out: dict = {}
    out["MaxImpact"] = (
        "NaN"
        if value.get("max_impact", 0) != value.get("max_impact", 0)
        else "Infinity"
        if value.get("max_impact", 0) == float("inf")
        else "-Infinity"
        if value.get("max_impact", 0) == float("-inf")
        else value.get("max_impact", 0)
    )
    out["TotalImpact"] = (
        "NaN"
        if value.get("total_impact", 0) != value.get("total_impact", 0)
        else "Infinity"
        if value.get("total_impact", 0) == float("inf")
        else "-Infinity"
        if value.get("total_impact", 0) == float("-inf")
        else value.get("total_impact", 0)
    )
    if "total_actual_spend" in value:
        out["TotalActualSpend"] = (
            "NaN"
            if value["total_actual_spend"] != value["total_actual_spend"]
            else "Infinity"
            if value["total_actual_spend"] == float("inf")
            else "-Infinity"
            if value["total_actual_spend"] == float("-inf")
            else value["total_actual_spend"]
        )
    if "total_expected_spend" in value:
        out["TotalExpectedSpend"] = (
            "NaN"
            if value["total_expected_spend"] != value["total_expected_spend"]
            else "Infinity"
            if value["total_expected_spend"] == float("inf")
            else "-Infinity"
            if value["total_expected_spend"] == float("-inf")
            else value["total_expected_spend"]
        )
    if "total_impact_percentage" in value:
        out["TotalImpactPercentage"] = (
            "NaN"
            if value["total_impact_percentage"] != value["total_impact_percentage"]
            else "Infinity"
            if value["total_impact_percentage"] == float("inf")
            else "-Infinity"
            if value["total_impact_percentage"] == float("-inf")
            else value["total_impact_percentage"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Impact:
    out: Impact = {}  # type: ignore[typeddict-item]
    if data.get("MaxImpact") is not None:
        out["max_impact"] = float(data["MaxImpact"])
    else:
        out["max_impact"] = 0
    if data.get("TotalImpact") is not None:
        out["total_impact"] = float(data["TotalImpact"])
    else:
        out["total_impact"] = 0
    if data.get("TotalActualSpend") is not None:
        out["total_actual_spend"] = float(data["TotalActualSpend"])
    if data.get("TotalExpectedSpend") is not None:
        out["total_expected_spend"] = float(data["TotalExpectedSpend"])
    if data.get("TotalImpactPercentage") is not None:
        out["total_impact_percentage"] = float(data["TotalImpactPercentage"])
    return out
