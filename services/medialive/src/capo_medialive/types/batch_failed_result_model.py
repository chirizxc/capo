"""Generated from Smithy shape ``com.amazonaws.medialive#BatchFailedResultModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class BatchFailedResultModel(TypedDict, closed=True):
    arn: NotRequired["capo_medialive.types.__string.__string"]
    """ARN of the resource"""
    code: NotRequired["capo_medialive.types.__string.__string"]
    """Error code for the failed operation"""
    id: NotRequired["capo_medialive.types.__string.__string"]
    """ID of the resource"""
    message: NotRequired["capo_medialive.types.__string.__string"]
    """Error message for the failed operation"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchFailedResultModel) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "code" in value:
        out["code"] = value["code"]
    if "id" in value:
        out["id"] = value["id"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchFailedResultModel:
    out: BatchFailedResultModel = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
