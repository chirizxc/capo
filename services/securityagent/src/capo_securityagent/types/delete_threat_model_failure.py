"""Generated from Smithy shape ``com.amazonaws.securityagent#DeleteThreatModelFailure``."""

from typing_extensions import NotRequired, TypedDict


class DeleteThreatModelFailure(TypedDict, closed=True):
    threat_model_id: NotRequired["str"]
    """<p>The unique identifier of the threat model that failed to delete.</p>"""
    reason: NotRequired["str"]
    """<p>The reason the threat model failed to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteThreatModelFailure) -> dict:
    out: dict = {}
    if "threat_model_id" in value:
        out["threatModelId"] = value["threat_model_id"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> DeleteThreatModelFailure:
    out: DeleteThreatModelFailure = {}  # type: ignore[typeddict-item]
    if data.get("threatModelId") is not None:
        out["threat_model_id"] = data["threatModelId"]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out
