"""Generated from Smithy shape ``com.amazonaws.medialive#BatchSuccessfulResultModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class BatchSuccessfulResultModel(TypedDict, closed=True):
    arn: NotRequired["capo_medialive.types.__string.__string"]
    """ARN of the resource"""
    id: NotRequired["capo_medialive.types.__string.__string"]
    """ID of the resource"""
    state: NotRequired["capo_medialive.types.__string.__string"]
    """Current state of the resource"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchSuccessfulResultModel) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "state" in value:
        out["state"] = value["state"]
    return out


def deserialize_json(data: dict) -> BatchSuccessfulResultModel:
    out: BatchSuccessfulResultModel = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("state") is not None:
        out["state"] = data["state"]
    return out
