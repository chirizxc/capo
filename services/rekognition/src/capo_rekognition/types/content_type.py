"""Generated from Smithy shape ``com.amazonaws.rekognition#ContentType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.percent
    import capo_rekognition.types.string


class ContentType(TypedDict, closed=True):
    confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>The confidence level of the label given</p>"""
    name: NotRequired["capo_rekognition.types.string.String"]
    """<p>The name of the label</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContentType) -> dict:
    out: dict = {}
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
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContentType:
    out: ContentType = {}  # type: ignore[typeddict-item]
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
