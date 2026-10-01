"""Generated from Smithy shape ``com.amazonaws.securityagent#GitLabResourceCapabilities``."""

from typing_extensions import NotRequired, TypedDict


class GitLabResourceCapabilities(TypedDict, closed=True):
    leave_comments: NotRequired["bool"]
    """<p>Whether to post code review comments on merge request discussions.</p>"""
    remediate_code: NotRequired["bool"]
    """<p>Whether to create merge requests with automated fixes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GitLabResourceCapabilities) -> dict:
    out: dict = {}
    if "leave_comments" in value:
        out["leaveComments"] = value["leave_comments"]
    if "remediate_code" in value:
        out["remediateCode"] = value["remediate_code"]
    return out


def deserialize_json(data: dict) -> GitLabResourceCapabilities:
    out: GitLabResourceCapabilities = {}  # type: ignore[typeddict-item]
    if data.get("leaveComments") is not None:
        out["leave_comments"] = data["leaveComments"]
    if data.get("remediateCode") is not None:
        out["remediate_code"] = data["remediateCode"]
    return out
