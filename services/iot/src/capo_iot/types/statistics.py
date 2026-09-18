"""Generated from Smithy shape ``com.amazonaws.iot#Statistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.average
    import capo_iot.types.count
    import capo_iot.types.maximum
    import capo_iot.types.minimum
    import capo_iot.types.std_deviation
    import capo_iot.types.sum
    import capo_iot.types.sum_of_squares
    import capo_iot.types.variance


class Statistics(TypedDict, closed=True):
    count: "capo_iot.types.count.Count"
    """<p>The count of things that match the query string criteria and contain a valid aggregation field value.</p>"""
    average: NotRequired["capo_iot.types.average.Average"]
    """<p>The average of the aggregated field values.</p>"""
    sum: NotRequired["capo_iot.types.sum.Sum"]
    """<p>The sum of the aggregated field values.</p>"""
    minimum: NotRequired["capo_iot.types.minimum.Minimum"]
    """<p>The minimum aggregated field value.</p>"""
    maximum: NotRequired["capo_iot.types.maximum.Maximum"]
    """<p>The maximum aggregated field value.</p>"""
    sum_of_squares: NotRequired["capo_iot.types.sum_of_squares.SumOfSquares"]
    """<p>The sum of the squares of the aggregated field values.</p>"""
    variance: NotRequired["capo_iot.types.variance.Variance"]
    """<p>The variance of the aggregated field values.</p>"""
    std_deviation: NotRequired["capo_iot.types.std_deviation.StdDeviation"]
    """<p>The standard deviation of the aggregated field values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Statistics) -> dict:
    out: dict = {}
    out["count"] = value.get("count", 0)
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
    if "sum_of_squares" in value:
        out["sumOfSquares"] = (
            "NaN"
            if value["sum_of_squares"] != value["sum_of_squares"]
            else "Infinity"
            if value["sum_of_squares"] == float("inf")
            else "-Infinity"
            if value["sum_of_squares"] == float("-inf")
            else value["sum_of_squares"]
        )
    if "variance" in value:
        out["variance"] = (
            "NaN"
            if value["variance"] != value["variance"]
            else "Infinity"
            if value["variance"] == float("inf")
            else "-Infinity"
            if value["variance"] == float("-inf")
            else value["variance"]
        )
    if "std_deviation" in value:
        out["stdDeviation"] = (
            "NaN"
            if value["std_deviation"] != value["std_deviation"]
            else "Infinity"
            if value["std_deviation"] == float("inf")
            else "-Infinity"
            if value["std_deviation"] == float("-inf")
            else value["std_deviation"]
        )
    return out


def deserialize_json(data: dict) -> Statistics:
    out: Statistics = {}  # type: ignore[typeddict-item]
    if data.get("count") is not None:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    if data.get("average") is not None:
        out["average"] = float(data["average"])
    if data.get("sum") is not None:
        out["sum"] = float(data["sum"])
    if data.get("minimum") is not None:
        out["minimum"] = float(data["minimum"])
    if data.get("maximum") is not None:
        out["maximum"] = float(data["maximum"])
    if data.get("sumOfSquares") is not None:
        out["sum_of_squares"] = float(data["sumOfSquares"])
    if data.get("variance") is not None:
        out["variance"] = float(data["variance"])
    if data.get("stdDeviation") is not None:
        out["std_deviation"] = float(data["stdDeviation"])
    return out
