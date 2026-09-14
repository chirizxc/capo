"""Generated from Smithy shape ``com.amazonaws.mwaa#StatisticSet``."""

from typing_extensions import NotRequired, TypedDict


class StatisticSet(TypedDict, closed=True):
    sample_count: NotRequired["int"]
    """<p> <b>Internal only</b>. The number of samples used for the statistic set.</p>"""
    sum: NotRequired["float"]
    """<p> <b>Internal only</b>. The sum of values for the sample set.</p>"""
    minimum: NotRequired["float"]
    """<p> <b>Internal only</b>. The minimum value of the sample set.</p>"""
    maximum: NotRequired["float"]
    """<p> <b>Internal only</b>. The maximum value of the sample set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatisticSet) -> dict:
    out: dict = {}
    if "sample_count" in value:
        out["SampleCount"] = value["sample_count"]
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
    if "minimum" in value:
        out["Minimum"] = (
            "NaN"
            if value["minimum"] != value["minimum"]
            else "Infinity"
            if value["minimum"] == float("inf")
            else "-Infinity"
            if value["minimum"] == float("-inf")
            else value["minimum"]
        )
    if "maximum" in value:
        out["Maximum"] = (
            "NaN"
            if value["maximum"] != value["maximum"]
            else "Infinity"
            if value["maximum"] == float("inf")
            else "-Infinity"
            if value["maximum"] == float("-inf")
            else value["maximum"]
        )
    return out


def deserialize_json(data: dict) -> StatisticSet:
    out: StatisticSet = {}  # type: ignore[typeddict-item]
    if data.get("SampleCount") is not None:
        out["sample_count"] = data["SampleCount"]
    if data.get("Sum") is not None:
        out["sum"] = float(data["Sum"])
    if data.get("Minimum") is not None:
        out["minimum"] = float(data["Minimum"])
    if data.get("Maximum") is not None:
        out["maximum"] = float(data["Maximum"])
    return out
