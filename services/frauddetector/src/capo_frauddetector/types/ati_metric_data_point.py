"""Generated from Smithy shape ``com.amazonaws.frauddetector#ATIMetricDataPoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.float


class ATIMetricDataPoint(TypedDict, closed=True):
    cr: NotRequired["capo_frauddetector.types.float.float"]
    """<p> The challenge rate. This indicates the percentage of login events that the model recommends to challenge such as one-time password, multi-factor authentication, and investigations. </p>"""
    adr: NotRequired["capo_frauddetector.types.float.float"]
    """<p> The anomaly discovery rate. This metric quantifies the percentage of anomalies that can be detected by the model at the selected score threshold. A lower score threshold increases the percentage of anomalies captured by the model, but would also require challenging a larger percentage of login events, leading to a higher customer friction. </p>"""
    threshold: NotRequired["capo_frauddetector.types.float.float"]
    """<p> The model's threshold that specifies an acceptable fraud capture rate. For example, a threshold of 500 means any model score 500 or above is labeled as fraud. </p>"""
    atodr: NotRequired["capo_frauddetector.types.float.float"]
    """<p> The account takeover discovery rate. This metric quantifies the percentage of account compromise events that can be detected by the model at the selected score threshold. This metric is only available if 50 or more entities with at-least one labeled account takeover event is present in the ingested dataset. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ATIMetricDataPoint) -> dict:
    out: dict = {}
    if "cr" in value:
        out["cr"] = (
            "NaN"
            if value["cr"] != value["cr"]
            else "Infinity"
            if value["cr"] == float("inf")
            else "-Infinity"
            if value["cr"] == float("-inf")
            else value["cr"]
        )
    if "adr" in value:
        out["adr"] = (
            "NaN"
            if value["adr"] != value["adr"]
            else "Infinity"
            if value["adr"] == float("inf")
            else "-Infinity"
            if value["adr"] == float("-inf")
            else value["adr"]
        )
    if "threshold" in value:
        out["threshold"] = (
            "NaN"
            if value["threshold"] != value["threshold"]
            else "Infinity"
            if value["threshold"] == float("inf")
            else "-Infinity"
            if value["threshold"] == float("-inf")
            else value["threshold"]
        )
    if "atodr" in value:
        out["atodr"] = (
            "NaN"
            if value["atodr"] != value["atodr"]
            else "Infinity"
            if value["atodr"] == float("inf")
            else "-Infinity"
            if value["atodr"] == float("-inf")
            else value["atodr"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ATIMetricDataPoint:
    out: ATIMetricDataPoint = {}  # type: ignore[typeddict-item]
    if data.get("cr") is not None:
        out["cr"] = float(data["cr"])
    if data.get("adr") is not None:
        out["adr"] = float(data["adr"])
    if data.get("threshold") is not None:
        out["threshold"] = float(data["threshold"])
    if data.get("atodr") is not None:
        out["atodr"] = float(data["atodr"])
    return out
