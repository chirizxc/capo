"""Generated from Smithy shape ``com.amazonaws.iotwireless#MetricQueryValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.avg
    import capo_iot_wireless.types.max
    import capo_iot_wireless.types.min
    import capo_iot_wireless.types.p90
    import capo_iot_wireless.types.std
    import capo_iot_wireless.types.sum


class MetricQueryValue(TypedDict, closed=True):
    min: NotRequired["capo_iot_wireless.types.min.Min"]
    """<p>The minimum of the values of all data points collected during the aggregation period.</p>"""
    max: NotRequired["capo_iot_wireless.types.max.Max"]
    """<p>The maximum of the values of all the data points collected during the aggregation period.</p>"""
    sum: NotRequired["capo_iot_wireless.types.sum.Sum"]
    """<p>The sum of the values of all data points collected during the aggregation period.</p>"""
    avg: NotRequired["capo_iot_wireless.types.avg.Avg"]
    """<p>The average of the values of all data points collected during the aggregation period.</p>"""
    std: NotRequired["capo_iot_wireless.types.std.Std"]
    """<p>The standard deviation of the values of all data points collected during the aggregation period.</p>"""
    p90: NotRequired["capo_iot_wireless.types.p90.P90"]
    """<p>The 90th percentile of the values of all data points collected during the aggregation period.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricQueryValue) -> dict:
    out: dict = {}
    if "min" in value:
        out["Min"] = (
            "NaN"
            if value["min"] != value["min"]
            else "Infinity"
            if value["min"] == float("inf")
            else "-Infinity"
            if value["min"] == float("-inf")
            else value["min"]
        )
    if "max" in value:
        out["Max"] = (
            "NaN"
            if value["max"] != value["max"]
            else "Infinity"
            if value["max"] == float("inf")
            else "-Infinity"
            if value["max"] == float("-inf")
            else value["max"]
        )
    if "sum" in value:
        out["Sum"] = (
            "NaN"
            if value["sum"] != value["sum"]
            else "Infinity"
            if value["sum"] == float("inf")
            else "-Infinity"
            if value["sum"] == float("-inf")
            else value["sum"]
        )
    if "avg" in value:
        out["Avg"] = (
            "NaN"
            if value["avg"] != value["avg"]
            else "Infinity"
            if value["avg"] == float("inf")
            else "-Infinity"
            if value["avg"] == float("-inf")
            else value["avg"]
        )
    if "std" in value:
        out["Std"] = (
            "NaN"
            if value["std"] != value["std"]
            else "Infinity"
            if value["std"] == float("inf")
            else "-Infinity"
            if value["std"] == float("-inf")
            else value["std"]
        )
    if "p90" in value:
        out["P90"] = (
            "NaN"
            if value["p90"] != value["p90"]
            else "Infinity"
            if value["p90"] == float("inf")
            else "-Infinity"
            if value["p90"] == float("-inf")
            else value["p90"]
        )
    return out


def deserialize_json(data: dict) -> MetricQueryValue:
    out: MetricQueryValue = {}  # type: ignore[typeddict-item]
    if data.get("Min") is not None:
        out["min"] = float(data["Min"])
    if data.get("Max") is not None:
        out["max"] = float(data["Max"])
    if data.get("Sum") is not None:
        out["sum"] = float(data["Sum"])
    if data.get("Avg") is not None:
        out["avg"] = float(data["Avg"])
    if data.get("Std") is not None:
        out["std"] = float(data["Std"])
    if data.get("P90") is not None:
        out["p90"] = float(data["P90"])
    return out
