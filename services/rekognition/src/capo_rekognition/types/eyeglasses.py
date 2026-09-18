"""Generated from Smithy shape ``com.amazonaws.rekognition#Eyeglasses``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.boolean
    import capo_rekognition.types.percent


class Eyeglasses(TypedDict, closed=True):
    value: "capo_rekognition.types.boolean.Boolean"
    """<p>Boolean value that indicates whether the face is wearing eye glasses or not.</p>"""
    confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>Level of confidence in the determination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Eyeglasses) -> dict:
    out: dict = {}
    out["Value"] = value.get("value", False)
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


def deserialize_aws_json_1_1(data: dict) -> Eyeglasses:
    out: Eyeglasses = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = False
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    return out
