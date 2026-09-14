"""Generated from Smithy shape ``com.amazonaws.forecastquery#DataPoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecastquery.types.double
    import capo_forecastquery.types.timestamp


class DataPoint(TypedDict, closed=True):
    timestamp: NotRequired["capo_forecastquery.types.timestamp.Timestamp"]
    """<p>The timestamp of the specific forecast.</p>"""
    value: NotRequired["capo_forecastquery.types.double.Double"]
    """<p>The forecast value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataPoint) -> dict:
    out: dict = {}
    if "timestamp" in value:
        out["Timestamp"] = value["timestamp"]
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


def deserialize_aws_json_1_1(data: dict) -> DataPoint:
    out: DataPoint = {}  # type: ignore[typeddict-item]
    if data.get("Timestamp") is not None:
        out["timestamp"] = data["Timestamp"]
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    return out
