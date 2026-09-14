"""Generated from Smithy shape ``com.amazonaws.frauddetector#MetricDataPoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.float


class MetricDataPoint(TypedDict, closed=True):
    fpr: NotRequired["capo_frauddetector.types.float.float"]
    """<p>The false positive rate. This is the percentage of total legitimate events that are incorrectly predicted as fraud.</p>"""
    precision: NotRequired["capo_frauddetector.types.float.float"]
    """<p>The percentage of fraud events correctly predicted as fraudulent as compared to all events predicted as fraudulent.</p>"""
    tpr: NotRequired["capo_frauddetector.types.float.float"]
    """<p>The true positive rate. This is the percentage of total fraud the model detects. Also known as capture rate.</p>"""
    threshold: NotRequired["capo_frauddetector.types.float.float"]
    """<p>The model threshold that specifies an acceptable fraud capture rate. For example, a threshold of 500 means any model score 500 or above is labeled as fraud.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricDataPoint) -> dict:
    out: dict = {}
    if "fpr" in value:
        out["fpr"] = (
            "NaN"
            if value["fpr"] != value["fpr"]
            else "Infinity"
            if value["fpr"] == float("inf")
            else "-Infinity"
            if value["fpr"] == float("-inf")
            else value["fpr"]
        )
    if "precision" in value:
        out["precision"] = (
            "NaN"
            if value["precision"] != value["precision"]
            else "Infinity"
            if value["precision"] == float("inf")
            else "-Infinity"
            if value["precision"] == float("-inf")
            else value["precision"]
        )
    if "tpr" in value:
        out["tpr"] = (
            "NaN"
            if value["tpr"] != value["tpr"]
            else "Infinity"
            if value["tpr"] == float("inf")
            else "-Infinity"
            if value["tpr"] == float("-inf")
            else value["tpr"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricDataPoint:
    out: MetricDataPoint = {}  # type: ignore[typeddict-item]
    if data.get("fpr") is not None:
        out["fpr"] = float(data["fpr"])
    if data.get("precision") is not None:
        out["precision"] = float(data["precision"])
    if data.get("tpr") is not None:
        out["tpr"] = float(data["tpr"])
    if data.get("threshold") is not None:
        out["threshold"] = float(data["threshold"])
    return out
