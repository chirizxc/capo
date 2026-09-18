"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Aggregates``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.aggregated_double_value


class Aggregates(TypedDict, closed=True):
    average: NotRequired[
        "capo_iotsitewise.types.aggregated_double_value.AggregatedDoubleValue"
    ]
    """<p>The average (mean) value of the time series over a time interval window.</p>"""
    count: NotRequired[
        "capo_iotsitewise.types.aggregated_double_value.AggregatedDoubleValue"
    ]
    """<p>The count of data points in the time series over a time interval window.</p>"""
    maximum: NotRequired[
        "capo_iotsitewise.types.aggregated_double_value.AggregatedDoubleValue"
    ]
    """<p>The maximum value of the time series over a time interval window.</p>"""
    minimum: NotRequired[
        "capo_iotsitewise.types.aggregated_double_value.AggregatedDoubleValue"
    ]
    """<p>The minimum value of the time series over a time interval window.</p>"""
    sum: NotRequired[
        "capo_iotsitewise.types.aggregated_double_value.AggregatedDoubleValue"
    ]
    """<p>The sum of the time series over a time interval window.</p>"""
    standard_deviation: NotRequired[
        "capo_iotsitewise.types.aggregated_double_value.AggregatedDoubleValue"
    ]
    """<p>The standard deviation of the time series over a time interval window.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Aggregates) -> dict:
    out: dict = {}
    if "average" in value:
        out["average"] = (
            "NaN"
            if value["average"] != value["average"]
            else "Infinity"
            if value["average"] == float("inf")
            else "-Infinity"
            if value["average"] == float("-inf")
            else value["average"]
        )
    if "count" in value:
        out["count"] = (
            "NaN"
            if value["count"] != value["count"]
            else "Infinity"
            if value["count"] == float("inf")
            else "-Infinity"
            if value["count"] == float("-inf")
            else value["count"]
        )
    if "maximum" in value:
        out["maximum"] = (
            "NaN"
            if value["maximum"] != value["maximum"]
            else "Infinity"
            if value["maximum"] == float("inf")
            else "-Infinity"
            if value["maximum"] == float("-inf")
            else value["maximum"]
        )
    if "minimum" in value:
        out["minimum"] = (
            "NaN"
            if value["minimum"] != value["minimum"]
            else "Infinity"
            if value["minimum"] == float("inf")
            else "-Infinity"
            if value["minimum"] == float("-inf")
            else value["minimum"]
        )
    if "sum" in value:
        out["sum"] = (
            "NaN"
            if value["sum"] != value["sum"]
            else "Infinity"
            if value["sum"] == float("inf")
            else "-Infinity"
            if value["sum"] == float("-inf")
            else value["sum"]
        )
    if "standard_deviation" in value:
        out["standardDeviation"] = (
            "NaN"
            if value["standard_deviation"] != value["standard_deviation"]
            else "Infinity"
            if value["standard_deviation"] == float("inf")
            else "-Infinity"
            if value["standard_deviation"] == float("-inf")
            else value["standard_deviation"]
        )
    return out


def deserialize_json(data: dict) -> Aggregates:
    out: Aggregates = {}  # type: ignore[typeddict-item]
    if data.get("average") is not None:
        out["average"] = float(data["average"])
    if data.get("count") is not None:
        out["count"] = float(data["count"])
    if data.get("maximum") is not None:
        out["maximum"] = float(data["maximum"])
    if data.get("minimum") is not None:
        out["minimum"] = float(data["minimum"])
    if data.get("sum") is not None:
        out["sum"] = float(data["sum"])
    if data.get("standardDeviation") is not None:
        out["standard_deviation"] = float(data["standardDeviation"])
    return out
