"""Generated from Smithy shape ``com.amazonaws.frauddetector#Detector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.description
    import capo_frauddetector.types.fraud_detector_arn
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.time


class Detector(TypedDict, closed=True):
    detector_id: NotRequired["capo_frauddetector.types.identifier.identifier"]
    """<p>The detector ID.</p>"""
    description: NotRequired["capo_frauddetector.types.description.description"]
    """<p>The detector description.</p>"""
    event_type_name: NotRequired["capo_frauddetector.types.identifier.identifier"]
    """<p>The name of the event type.</p>"""
    last_updated_time: NotRequired["capo_frauddetector.types.time.time"]
    """<p>Timestamp of when the detector was last updated.</p>"""
    created_time: NotRequired["capo_frauddetector.types.time.time"]
    """<p>Timestamp of when the detector was created.</p>"""
    arn: NotRequired["capo_frauddetector.types.fraud_detector_arn.fraudDetectorArn"]
    """<p>The detector ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Detector) -> dict:
    out: dict = {}
    if "detector_id" in value:
        out["detectorId"] = value["detector_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "event_type_name" in value:
        out["eventTypeName"] = value["event_type_name"]
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    if "created_time" in value:
        out["createdTime"] = value["created_time"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Detector:
    out: Detector = {}  # type: ignore[typeddict-item]
    if data.get("detectorId") is not None:
        out["detector_id"] = data["detectorId"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("eventTypeName") is not None:
        out["event_type_name"] = data["eventTypeName"]
    if data.get("lastUpdatedTime") is not None:
        out["last_updated_time"] = data["lastUpdatedTime"]
    if data.get("createdTime") is not None:
        out["created_time"] = data["createdTime"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    return out
