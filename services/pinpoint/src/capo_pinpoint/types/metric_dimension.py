"""Generated from Smithy shape ``com.amazonaws.pinpoint#MetricDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__double
    import capo_pinpoint.types.__string


class MetricDimension(TypedDict, closed=True):
    comparison_operator: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The operator to use when comparing metric values. Valid values are: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, and EQUAL.</p>"""
    value: NotRequired["capo_pinpoint.types.__double.__double"]
    """<p>The value to compare.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricDimension) -> dict:
    out: dict = {}
    if "comparison_operator" in value:
        out["ComparisonOperator"] = value["comparison_operator"]
    if "value" in value:
        out["Value"] = (
            "NaN"
            if value["value"] != value["value"]
            else "Infinity"
            if value["value"] == float("inf")
            else "-Infinity"
            if value["value"] == float("-inf")
            else value["value"]
        )
    return out


def deserialize_json(data: dict) -> MetricDimension:
    out: MetricDimension = {}  # type: ignore[typeddict-item]
    if data.get("ComparisonOperator") is not None:
        out["comparison_operator"] = data["ComparisonOperator"]
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    return out
