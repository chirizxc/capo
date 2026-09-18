"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectLabelsImageQuality``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.float


class DetectLabelsImageQuality(TypedDict, closed=True):
    brightness: NotRequired["capo_rekognition.types.float.Float"]
    """<p>The brightness of an image provided for label detection.</p>"""
    sharpness: NotRequired["capo_rekognition.types.float.Float"]
    """<p>The sharpness of an image provided for label detection.</p>"""
    contrast: NotRequired["capo_rekognition.types.float.Float"]
    """<p>The contrast of an image provided for label detection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectLabelsImageQuality) -> dict:
    out: dict = {}
    if "brightness" in value:
        out["Brightness"] = (
            "NaN"
            if value["brightness"] != value["brightness"]
            else "Infinity"
            if value["brightness"] == float("inf")
            else "-Infinity"
            if value["brightness"] == float("-inf")
            else value["brightness"]
        )
    if "sharpness" in value:
        out["Sharpness"] = (
            "NaN"
            if value["sharpness"] != value["sharpness"]
            else "Infinity"
            if value["sharpness"] == float("inf")
            else "-Infinity"
            if value["sharpness"] == float("-inf")
            else value["sharpness"]
        )
    if "contrast" in value:
        out["Contrast"] = (
            "NaN"
            if value["contrast"] != value["contrast"]
            else "Infinity"
            if value["contrast"] == float("inf")
            else "-Infinity"
            if value["contrast"] == float("-inf")
            else value["contrast"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectLabelsImageQuality:
    out: DetectLabelsImageQuality = {}  # type: ignore[typeddict-item]
    if data.get("Brightness") is not None:
        out["brightness"] = float(data["Brightness"])
    if data.get("Sharpness") is not None:
        out["sharpness"] = float(data["Sharpness"])
    if data.get("Contrast") is not None:
        out["contrast"] = float(data["Contrast"])
    return out
