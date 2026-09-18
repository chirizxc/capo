"""Generated from Smithy shape ``com.amazonaws.rekognition#CustomLabel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.geometry
    import capo_rekognition.types.percent
    import capo_rekognition.types.string


class CustomLabel(TypedDict, closed=True):
    name: NotRequired["capo_rekognition.types.string.String"]
    """<p>The name of the custom label.</p>"""
    confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>The confidence that the model has in the detection of the custom label. The range is 0-100. A higher value indicates a higher confidence.</p>"""
    geometry: NotRequired["capo_rekognition.types.geometry.Geometry"]
    """<p>The location of the detected object on the image that corresponds to the custom label. Includes an axis aligned coarse bounding box surrounding the object and a finer grain polygon for more accurate spatial information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomLabel) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
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
    if "geometry" in value:
        import capo_rekognition.types.geometry

        out["Geometry"] = capo_rekognition.types.geometry.serialize_aws_json_1_1(
            value["geometry"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomLabel:
    out: CustomLabel = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    if data.get("Geometry") is not None:
        import capo_rekognition.types.geometry

        out["geometry"] = capo_rekognition.types.geometry.deserialize_aws_json_1_1(
            data["Geometry"]
        )
    return out
