"""Generated from Smithy shape ``com.amazonaws.rekognition#EyeDirection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.degree
    import capo_rekognition.types.percent


class EyeDirection(TypedDict, closed=True):
    yaw: NotRequired["capo_rekognition.types.degree.Degree"]
    """<p>Value representing eye direction on the yaw axis.</p>"""
    pitch: NotRequired["capo_rekognition.types.degree.Degree"]
    """<p>Value representing eye direction on the pitch axis.</p>"""
    confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>The confidence that the service has in its predicted eye direction.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EyeDirection) -> dict:
    out: dict = {}
    if "yaw" in value:
        out["Yaw"] = (
            "NaN"
            if value["yaw"] != value["yaw"]
            else "Infinity"
            if value["yaw"] == float("inf")
            else "-Infinity"
            if value["yaw"] == float("-inf")
            else value["yaw"]
        )
    if "pitch" in value:
        out["Pitch"] = (
            "NaN"
            if value["pitch"] != value["pitch"]
            else "Infinity"
            if value["pitch"] == float("inf")
            else "-Infinity"
            if value["pitch"] == float("-inf")
            else value["pitch"]
        )
    if "confidence" in value:
        out["Confidence"] = (
            "NaN"
            if value["confidence"] != value["confidence"]
            else "Infinity"
            if value["confidence"] == float("inf")
            else "-Infinity"
            if value["confidence"] == float("-inf")
            else value["confidence"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EyeDirection:
    out: EyeDirection = {}  # type: ignore[typeddict-item]
    if data.get("Yaw") is not None:
        out["yaw"] = float(data["Yaw"])
    if data.get("Pitch") is not None:
        out["pitch"] = float(data["Pitch"])
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    return out
