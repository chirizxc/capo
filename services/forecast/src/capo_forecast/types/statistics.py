"""Generated from Smithy shape ``com.amazonaws.forecast#Statistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.double
    import capo_forecast.types.integer
    import capo_forecast.types.long
    import capo_forecast.types.string


class Statistics(TypedDict, closed=True):
    count: NotRequired["capo_forecast.types.integer.Integer"]
    """<p>The number of values in the field. If the response value is -1, refer to <code>CountLong</code>.</p>"""
    count_distinct: NotRequired["capo_forecast.types.integer.Integer"]
    """<p>The number of distinct values in the field. If the response value is -1, refer to <code>CountDistinctLong</code>.</p>"""
    count_null: NotRequired["capo_forecast.types.integer.Integer"]
    """<p>The number of null values in the field. If the response value is -1, refer to <code>CountNullLong</code>.</p>"""
    count_nan: NotRequired["capo_forecast.types.integer.Integer"]
    """<p>The number of NAN (not a number) values in the field. If the response value is -1, refer to <code>CountNanLong</code>.</p>"""
    min: NotRequired["capo_forecast.types.string.String"]
    """<p>For a numeric field, the minimum value in the field.</p>"""
    max: NotRequired["capo_forecast.types.string.String"]
    """<p>For a numeric field, the maximum value in the field.</p>"""
    avg: NotRequired["capo_forecast.types.double.Double"]
    """<p>For a numeric field, the average value in the field.</p>"""
    stddev: NotRequired["capo_forecast.types.double.Double"]
    """<p>For a numeric field, the standard deviation.</p>"""
    count_long: NotRequired["capo_forecast.types.long.Long"]
    """<p>The number of values in the field. <code>CountLong</code> is used instead of <code>Count</code> if the value is greater than 2,147,483,647.</p>"""
    count_distinct_long: NotRequired["capo_forecast.types.long.Long"]
    """<p>The number of distinct values in the field. <code>CountDistinctLong</code> is used instead of <code>CountDistinct</code> if the value is greater than 2,147,483,647.</p>"""
    count_null_long: NotRequired["capo_forecast.types.long.Long"]
    """<p>The number of null values in the field. <code>CountNullLong</code> is used instead of <code>CountNull</code> if the value is greater than 2,147,483,647.</p>"""
    count_nan_long: NotRequired["capo_forecast.types.long.Long"]
    """<p>The number of NAN (not a number) values in the field. <code>CountNanLong</code> is used instead of <code>CountNan</code> if the value is greater than 2,147,483,647.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Statistics) -> dict:
    out: dict = {}
    if "count" in value:
        out["Count"] = value["count"]
    if "count_distinct" in value:
        out["CountDistinct"] = value["count_distinct"]
    if "count_null" in value:
        out["CountNull"] = value["count_null"]
    if "count_nan" in value:
        out["CountNan"] = value["count_nan"]
    if "min" in value:
        out["Min"] = value["min"]
    if "max" in value:
        out["Max"] = value["max"]
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
    if "stddev" in value:
        out["Stddev"] = (
            "NaN"
            if value["stddev"] != value["stddev"]
            else "Infinity"
            if value["stddev"] == float("inf")
            else "-Infinity"
            if value["stddev"] == float("-inf")
            else value["stddev"]
        )
    if "count_long" in value:
        out["CountLong"] = value["count_long"]
    if "count_distinct_long" in value:
        out["CountDistinctLong"] = value["count_distinct_long"]
    if "count_null_long" in value:
        out["CountNullLong"] = value["count_null_long"]
    if "count_nan_long" in value:
        out["CountNanLong"] = value["count_nan_long"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Statistics:
    out: Statistics = {}  # type: ignore[typeddict-item]
    if data.get("Count") is not None:
        out["count"] = data["Count"]
    if data.get("CountDistinct") is not None:
        out["count_distinct"] = data["CountDistinct"]
    if data.get("CountNull") is not None:
        out["count_null"] = data["CountNull"]
    if data.get("CountNan") is not None:
        out["count_nan"] = data["CountNan"]
    if data.get("Min") is not None:
        out["min"] = data["Min"]
    if data.get("Max") is not None:
        out["max"] = data["Max"]
    if data.get("Avg") is not None:
        out["avg"] = float(data["Avg"])
    if data.get("Stddev") is not None:
        out["stddev"] = float(data["Stddev"])
    if data.get("CountLong") is not None:
        out["count_long"] = data["CountLong"]
    if data.get("CountDistinctLong") is not None:
        out["count_distinct_long"] = data["CountDistinctLong"]
    if data.get("CountNullLong") is not None:
        out["count_null_long"] = data["CountNullLong"]
    if data.get("CountNanLong") is not None:
        out["count_nan_long"] = data["CountNanLong"]
    return out
