"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BatchDeleteSuccessfulDeletion``."""

from typing_extensions import NotRequired, TypedDict


class BatchDeleteSuccessfulDeletion(TypedDict, closed=True):
    resource_arn: NotRequired["str"]
    """ARN of the deleted configuration (populated only when deleting by ARN list)."""
    signal_type: NotRequired["str"]
    """Signal type of the deleted configuration (populated only when deleting by scope)."""
    location_hash: NotRequired["str"]
    """Location hash of the deleted configuration (populated only when deleting by scope)."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteSuccessfulDeletion) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "signal_type" in value:
        out["SignalType"] = value["signal_type"]
    if "location_hash" in value:
        out["LocationHash"] = value["location_hash"]
    return out


def deserialize_json(data: dict) -> BatchDeleteSuccessfulDeletion:
    out: BatchDeleteSuccessfulDeletion = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("SignalType") is not None:
        out["signal_type"] = data["SignalType"]
    if data.get("LocationHash") is not None:
        out["location_hash"] = data["LocationHash"]
    return out
