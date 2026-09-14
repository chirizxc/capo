"""Generated from Smithy shape ``com.amazonaws.frauddetector#Outcome``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.description
    import capo_frauddetector.types.fraud_detector_arn
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.time


class Outcome(TypedDict, closed=True):
    name: NotRequired["capo_frauddetector.types.identifier.identifier"]
    """<p>The outcome name.</p>"""
    description: NotRequired["capo_frauddetector.types.description.description"]
    """<p>The outcome description.</p>"""
    last_updated_time: NotRequired["capo_frauddetector.types.time.time"]
    """<p>The timestamp when the outcome was last updated.</p>"""
    created_time: NotRequired["capo_frauddetector.types.time.time"]
    """<p>The timestamp when the outcome was created.</p>"""
    arn: NotRequired["capo_frauddetector.types.fraud_detector_arn.fraudDetectorArn"]
    """<p>The outcome ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Outcome) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    if "created_time" in value:
        out["createdTime"] = value["created_time"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Outcome:
    out: Outcome = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("lastUpdatedTime") is not None:
        out["last_updated_time"] = data["lastUpdatedTime"]
    if data.get("createdTime") is not None:
        out["created_time"] = data["createdTime"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    return out
