"""Generated from Smithy shape ``com.amazonaws.rekognition#UnsuccessfulFaceAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.face_id
    import capo_rekognition.types.percent
    import capo_rekognition.types.unsuccessful_face_association_reasons
    import capo_rekognition.types.user_id


class UnsuccessfulFaceAssociation(TypedDict, closed=True):
    face_id: NotRequired["capo_rekognition.types.face_id.FaceId"]
    """<p>A unique identifier assigned to the face. </p>"""
    user_id: NotRequired["capo_rekognition.types.user_id.UserId"]
    """<p>A provided ID for the UserID. Unique within the collection. </p>"""
    confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>Match confidence with the UserID, provides information regarding if a face association was unsuccessful because it didn't meet UserMatchThreshold.</p>"""
    reasons: NotRequired[
        "capo_rekognition.types.unsuccessful_face_association_reasons.UnsuccessfulFaceAssociationReasons"
    ]
    """<p> The reason why the association was unsuccessful. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsuccessfulFaceAssociation) -> dict:
    out: dict = {}
    if "face_id" in value:
        out["FaceId"] = value["face_id"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
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
    if "reasons" in value:
        import capo_rekognition.types.unsuccessful_face_association_reasons

        out["Reasons"] = (
            capo_rekognition.types.unsuccessful_face_association_reasons.serialize_aws_json_1_1(
                value["reasons"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsuccessfulFaceAssociation:
    out: UnsuccessfulFaceAssociation = {}  # type: ignore[typeddict-item]
    if data.get("FaceId") is not None:
        out["face_id"] = data["FaceId"]
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    if data.get("Reasons") is not None:
        import capo_rekognition.types.unsuccessful_face_association_reasons

        out["reasons"] = (
            capo_rekognition.types.unsuccessful_face_association_reasons.deserialize_aws_json_1_1(
                data["Reasons"]
            )
        )
    return out
