"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.bounding_box_height
    import capo_rekognition.types.bounding_box_width
    import capo_rekognition.types.percent


class DetectionFilter(TypedDict, closed=True):
    min_confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>Sets the confidence of word detection. Words with detection confidence below this will be excluded from the result. Values should be between 0 and 100. The default MinConfidence is 80.</p>"""
    min_bounding_box_height: NotRequired[
        "capo_rekognition.types.bounding_box_height.BoundingBoxHeight"
    ]
    """<p>Sets the minimum height of the word bounding box. Words with bounding box heights lesser than this value will be excluded from the result. Value is relative to the video frame height.</p>"""
    min_bounding_box_width: NotRequired[
        "capo_rekognition.types.bounding_box_width.BoundingBoxWidth"
    ]
    """<p>Sets the minimum width of the word bounding box. Words with bounding boxes widths lesser than this value will be excluded from the result. Value is relative to the video frame width.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectionFilter) -> dict:
    out: dict = {}
    if "min_confidence" in value:
        out["MinConfidence"] = (
            "NaN"
            if value["min_confidence"] != value["min_confidence"]
            else "Infinity"
            if value["min_confidence"] == float("inf")
            else "-Infinity"
            if value["min_confidence"] == float("-inf")
            else value["min_confidence"]
        )
    if "min_bounding_box_height" in value:
        out["MinBoundingBoxHeight"] = (
            "NaN"
            if value["min_bounding_box_height"] != value["min_bounding_box_height"]
            else "Infinity"
            if value["min_bounding_box_height"] == float("inf")
            else "-Infinity"
            if value["min_bounding_box_height"] == float("-inf")
            else value["min_bounding_box_height"]
        )
    if "min_bounding_box_width" in value:
        out["MinBoundingBoxWidth"] = (
            "NaN"
            if value["min_bounding_box_width"] != value["min_bounding_box_width"]
            else "Infinity"
            if value["min_bounding_box_width"] == float("inf")
            else "-Infinity"
            if value["min_bounding_box_width"] == float("-inf")
            else value["min_bounding_box_width"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectionFilter:
    out: DetectionFilter = {}  # type: ignore[typeddict-item]
    if data.get("MinConfidence") is not None:
        out["min_confidence"] = float(data["MinConfidence"])
    if data.get("MinBoundingBoxHeight") is not None:
        out["min_bounding_box_height"] = float(data["MinBoundingBoxHeight"])
    if data.get("MinBoundingBoxWidth") is not None:
        out["min_bounding_box_width"] = float(data["MinBoundingBoxWidth"])
    return out
