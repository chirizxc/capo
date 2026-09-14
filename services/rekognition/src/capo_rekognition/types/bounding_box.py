"""Generated from Smithy shape ``com.amazonaws.rekognition#BoundingBox``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.float


class BoundingBox(TypedDict, closed=True):
    width: NotRequired["capo_rekognition.types.float.Float"]
    """<p>Width of the bounding box as a ratio of the overall image width.</p>"""
    height: NotRequired["capo_rekognition.types.float.Float"]
    """<p>Height of the bounding box as a ratio of the overall image height.</p>"""
    left: NotRequired["capo_rekognition.types.float.Float"]
    """<p>Left coordinate of the bounding box as a ratio of overall image width.</p>"""
    top: NotRequired["capo_rekognition.types.float.Float"]
    """<p>Top coordinate of the bounding box as a ratio of overall image height.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BoundingBox) -> dict:
    out: dict = {}
    if "width" in value:
        out["Width"] = (
            "NaN"
            if value["width"] != value["width"]
            else "Infinity"
            if value["width"] == float("inf")
            else "-Infinity"
            if value["width"] == float("-inf")
            else value["width"]
        )
    if "height" in value:
        out["Height"] = (
            "NaN"
            if value["height"] != value["height"]
            else "Infinity"
            if value["height"] == float("inf")
            else "-Infinity"
            if value["height"] == float("-inf")
            else value["height"]
        )
    if "left" in value:
        out["Left"] = (
            "NaN"
            if value["left"] != value["left"]
            else "Infinity"
            if value["left"] == float("inf")
            else "-Infinity"
            if value["left"] == float("-inf")
            else value["left"]
        )
    if "top" in value:
        out["Top"] = (
            "NaN"
            if value["top"] != value["top"]
            else "Infinity"
            if value["top"] == float("inf")
            else "-Infinity"
            if value["top"] == float("-inf")
            else value["top"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BoundingBox:
    out: BoundingBox = {}  # type: ignore[typeddict-item]
    if data.get("Width") is not None:
        out["width"] = float(data["Width"])
    if data.get("Height") is not None:
        out["height"] = float(data["Height"])
    if data.get("Left") is not None:
        out["left"] = float(data["Left"])
    if data.get("Top") is not None:
        out["top"] = float(data["Top"])
    return out
