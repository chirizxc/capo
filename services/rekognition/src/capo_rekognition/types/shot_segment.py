"""Generated from Smithy shape ``com.amazonaws.rekognition#ShotSegment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.segment_confidence
    import capo_rekognition.types.u_long


class ShotSegment(TypedDict, closed=True):
    index: NotRequired["capo_rekognition.types.u_long.ULong"]
    """<p>An Identifier for a shot detection segment detected in a video. </p>"""
    confidence: NotRequired[
        "capo_rekognition.types.segment_confidence.SegmentConfidence"
    ]
    """<p>The confidence that Amazon Rekognition Video has in the accuracy of the detected segment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShotSegment) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
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


def deserialize_aws_json_1_1(data: dict) -> ShotSegment:
    out: ShotSegment = {}  # type: ignore[typeddict-item]
    if data.get("Index") is not None:
        out["index"] = data["Index"]
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    return out
