"""Generated from Smithy shape ``com.amazonaws.datazone#FailureReason``."""

from typing_extensions import NotRequired, TypedDict


class FailureReason(TypedDict, closed=True):
    id: NotRequired["str"]
    """<p>The identifier of the resource that failed to delete.</p>"""
    message: NotRequired["str"]
    """<p>The error message associated with the resource that failed to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailureReason) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> FailureReason:
    out: FailureReason = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
