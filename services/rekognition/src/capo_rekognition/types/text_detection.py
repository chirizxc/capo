"""Generated from Smithy shape ``com.amazonaws.rekognition#TextDetection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.geometry
    import capo_rekognition.types.percent
    import capo_rekognition.types.string
    import capo_rekognition.types.text_types
    import capo_rekognition.types.u_integer


class TextDetection(TypedDict, closed=True):
    detected_text: NotRequired["capo_rekognition.types.string.String"]
    """<p>The word or line of text recognized by Amazon Rekognition. </p>"""
    type: NotRequired["capo_rekognition.types.text_types.TextTypes"]
    """<p>The type of text that was detected.</p>"""
    id: NotRequired["capo_rekognition.types.u_integer.UInteger"]
    """<p>The identifier for the detected text. The identifier is only unique for a single call to <code>DetectText</code>. </p>"""
    parent_id: NotRequired["capo_rekognition.types.u_integer.UInteger"]
    """<p>The Parent identifier for the detected text identified by the value of <code>ID</code>. If the type of detected text is <code>LINE</code>, the value of <code>ParentId</code> is <code>Null</code>. </p>"""
    confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>The confidence that Amazon Rekognition has in the accuracy of the detected text and the accuracy of the geometry points around the detected text.</p>"""
    geometry: NotRequired["capo_rekognition.types.geometry.Geometry"]
    """<p>The location of the detected text on the image. Includes an axis aligned coarse bounding box surrounding the text and a finer grain polygon for more accurate spatial information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextDetection) -> dict:
    out: dict = {}
    if "detected_text" in value:
        out["DetectedText"] = value["detected_text"]
    if "type" in value:
        import capo_rekognition.types.text_types

        out["Type"] = capo_rekognition.types.text_types.serialize_aws_json_1_1(
            value["type"]
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "parent_id" in value:
        out["ParentId"] = value["parent_id"]
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


def deserialize_aws_json_1_1(data: dict) -> TextDetection:
    out: TextDetection = {}  # type: ignore[typeddict-item]
    if data.get("DetectedText") is not None:
        out["detected_text"] = data["DetectedText"]
    if data.get("Type") is not None:
        import capo_rekognition.types.text_types

        out["type"] = capo_rekognition.types.text_types.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("ParentId") is not None:
        out["parent_id"] = data["ParentId"]
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    if data.get("Geometry") is not None:
        import capo_rekognition.types.geometry

        out["geometry"] = capo_rekognition.types.geometry.deserialize_aws_json_1_1(
            data["Geometry"]
        )
    return out
