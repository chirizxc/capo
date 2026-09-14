"""Generated from Smithy shape ``com.amazonaws.connect#MetricDataV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.metric_v2
    import capo_connect.types.value


class MetricDataV2(TypedDict, closed=True):
    metric: NotRequired["capo_connect.types.metric_v2.MetricV2"]
    """<p>The metric name or metricId, thresholds, and metric filters of the returned metric.</p>"""
    value: NotRequired["capo_connect.types.value.Value"]
    """<p>The corresponding value of the metric returned in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricDataV2) -> dict:
    out: dict = {}
    if "metric" in value:
        import capo_connect.types.metric_v2

        out["Metric"] = capo_connect.types.metric_v2.serialize_json(value["metric"])
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


def deserialize_json(data: dict) -> MetricDataV2:
    out: MetricDataV2 = {}  # type: ignore[typeddict-item]
    if data.get("Metric") is not None:
        import capo_connect.types.metric_v2

        out["metric"] = capo_connect.types.metric_v2.deserialize_json(data["Metric"])
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    return out
