"""Generated from Smithy shape ``com.amazonaws.forecast#BaselineMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.double
    import capo_forecast.types.name


class BaselineMetric(TypedDict, closed=True):
    name: NotRequired["capo_forecast.types.name.Name"]
    """<p>The name of the metric.</p>"""
    value: NotRequired["capo_forecast.types.double.Double"]
    """<p>The value for the metric.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BaselineMetric) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
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


def deserialize_aws_json_1_1(data: dict) -> BaselineMetric:
    out: BaselineMetric = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    return out
