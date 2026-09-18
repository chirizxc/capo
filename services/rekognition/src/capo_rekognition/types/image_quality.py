"""Generated from Smithy shape ``com.amazonaws.rekognition#ImageQuality``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.float


class ImageQuality(TypedDict, closed=True):
    brightness: NotRequired["capo_rekognition.types.float.Float"]
    """<p>Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.</p>"""
    sharpness: NotRequired["capo_rekognition.types.float.Float"]
    """<p>Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageQuality) -> dict:
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
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageQuality:
    out: ImageQuality = {}  # type: ignore[typeddict-item]
    if data.get("Brightness") is not None:
        out["brightness"] = float(data["Brightness"])
    if data.get("Sharpness") is not None:
        out["sharpness"] = float(data["Sharpness"])
    return out
