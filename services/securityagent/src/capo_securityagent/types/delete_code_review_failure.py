"""Generated from Smithy shape ``com.amazonaws.securityagent#DeleteCodeReviewFailure``."""

from typing_extensions import NotRequired, TypedDict


class DeleteCodeReviewFailure(TypedDict, closed=True):
    code_review_id: NotRequired["str"]
    """<p>The unique identifier of the code review that failed to delete.</p>"""
    reason: NotRequired["str"]
    """<p>The reason the code review failed to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCodeReviewFailure) -> dict:
    out: dict = {}
    if "code_review_id" in value:
        out["codeReviewId"] = value["code_review_id"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> DeleteCodeReviewFailure:
    out: DeleteCodeReviewFailure = {}  # type: ignore[typeddict-item]
    if data.get("codeReviewId") is not None:
        out["code_review_id"] = data["codeReviewId"]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out
