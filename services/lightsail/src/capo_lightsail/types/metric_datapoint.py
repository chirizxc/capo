"""Generated from Smithy shape ``com.amazonaws.lightsail#MetricDatapoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.double
    import capo_lightsail.types.metric_unit
    import capo_lightsail.types.timestamp


class MetricDatapoint(TypedDict, closed=True):
    average: NotRequired["capo_lightsail.types.double.double"]
    """<p>The average.</p>"""
    maximum: NotRequired["capo_lightsail.types.double.double"]
    """<p>The maximum.</p>"""
    minimum: NotRequired["capo_lightsail.types.double.double"]
    """<p>The minimum.</p>"""
    sample_count: NotRequired["capo_lightsail.types.double.double"]
    """<p>The sample count.</p>"""
    sum: NotRequired["capo_lightsail.types.double.double"]
    """<p>The sum.</p>"""
    timestamp: NotRequired["capo_lightsail.types.timestamp.timestamp"]
    """<p>The timestamp (<code>1479816991.349</code>).</p>"""
    unit: NotRequired["capo_lightsail.types.metric_unit.MetricUnit"]
    """<p>The unit. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricDatapoint) -> dict:
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
    if "sample_count" in value:
        out["sampleCount"] = (
            "NaN"
            if value["sample_count"] != value["sample_count"]
            else "Infinity"
            if value["sample_count"] == float("inf")
            else "-Infinity"
            if value["sample_count"] == float("-inf")
            else value["sample_count"]
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
    if "timestamp" in value:
        import capo_lightsail.types.timestamp

        out["timestamp"] = capo_lightsail.types.timestamp.serialize_aws_json_1_1(
            value["timestamp"]
        )
    if "unit" in value:
        import capo_lightsail.types.metric_unit

        out["unit"] = capo_lightsail.types.metric_unit.serialize_aws_json_1_1(
            value["unit"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricDatapoint:
    out: MetricDatapoint = {}  # type: ignore[typeddict-item]
    if data.get("average") is not None:
        out["average"] = float(data["average"])
    if data.get("maximum") is not None:
        out["maximum"] = float(data["maximum"])
    if data.get("minimum") is not None:
        out["minimum"] = float(data["minimum"])
    if data.get("sampleCount") is not None:
        out["sample_count"] = float(data["sampleCount"])
    if data.get("sum") is not None:
        out["sum"] = float(data["sum"])
    if data.get("timestamp") is not None:
        import capo_lightsail.types.timestamp

        out["timestamp"] = capo_lightsail.types.timestamp.deserialize_aws_json_1_1(
            data["timestamp"]
        )
    if data.get("unit") is not None:
        import capo_lightsail.types.metric_unit

        out["unit"] = capo_lightsail.types.metric_unit.deserialize_aws_json_1_1(
            data["unit"]
        )
    return out
