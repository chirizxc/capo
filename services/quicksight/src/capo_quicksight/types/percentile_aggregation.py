"""Generated from Smithy shape ``com.amazonaws.quicksight#PercentileAggregation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.percentile_value


class PercentileAggregation(TypedDict, closed=True):
    percentile_value: NotRequired[
        "capo_quicksight.types.percentile_value.PercentileValue"
    ]
    """<p>The percentile value. This value can be any numeric constant 0–100. A percentile value of 50 computes the median value of the measure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PercentileAggregation) -> dict:
    out: dict = {}
    if "percentile_value" in value:
        out["PercentileValue"] = (
            "NaN"
            if value["percentile_value"] != value["percentile_value"]
            else "Infinity"
            if value["percentile_value"] == float("inf")
            else "-Infinity"
            if value["percentile_value"] == float("-inf")
            else value["percentile_value"]
        )
    return out


def deserialize_json(data: dict) -> PercentileAggregation:
    out: PercentileAggregation = {}  # type: ignore[typeddict-item]
    if data.get("PercentileValue") is not None:
        out["percentile_value"] = float(data["PercentileValue"])
    return out
