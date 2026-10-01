"""Generated from Smithy shape ``com.amazonaws.securityagent#BitbucketResourceCapabilities``."""

from typing_extensions import NotRequired, TypedDict


class BitbucketResourceCapabilities(TypedDict, closed=True):
    leave_comments: NotRequired["bool"]
    """<p>Whether to post code review comments on pull requests.</p>"""
    remediate_code: NotRequired["bool"]
    """<p>Whether to create pull requests with automated fixes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BitbucketResourceCapabilities) -> dict:
    out: dict = {}
    if "leave_comments" in value:
        out["leaveComments"] = value["leave_comments"]
    if "remediate_code" in value:
        out["remediateCode"] = value["remediate_code"]
    return out


def deserialize_json(data: dict) -> BitbucketResourceCapabilities:
    out: BitbucketResourceCapabilities = {}  # type: ignore[typeddict-item]
    if data.get("leaveComments") is not None:
        out["leave_comments"] = data["leaveComments"]
    if data.get("remediateCode") is not None:
        out["remediate_code"] = data["remediateCode"]
    return out
