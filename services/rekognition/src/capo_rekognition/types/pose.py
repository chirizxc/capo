"""Generated from Smithy shape ``com.amazonaws.rekognition#Pose``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.degree


class Pose(TypedDict, closed=True):
    roll: NotRequired["capo_rekognition.types.degree.Degree"]
    """<p>Value representing the face rotation on the roll axis.</p>"""
    yaw: NotRequired["capo_rekognition.types.degree.Degree"]
    """<p>Value representing the face rotation on the yaw axis.</p>"""
    pitch: NotRequired["capo_rekognition.types.degree.Degree"]
    """<p>Value representing the face rotation on the pitch axis.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Pose) -> dict:
    out: dict = {}
    if "roll" in value:
        out["Roll"] = (
            "NaN"
            if value["roll"] != value["roll"]
            else "Infinity"
            if value["roll"] == float("inf")
            else "-Infinity"
            if value["roll"] == float("-inf")
            else value["roll"]
        )
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
    return out


def deserialize_aws_json_1_1(data: dict) -> Pose:
    out: Pose = {}  # type: ignore[typeddict-item]
    if data.get("Roll") is not None:
        out["roll"] = float(data["Roll"])
    if data.get("Yaw") is not None:
        out["yaw"] = float(data["Yaw"])
    if data.get("Pitch") is not None:
        out["pitch"] = float(data["Pitch"])
    return out
