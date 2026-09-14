"""Generated from Smithy shape ``com.amazonaws.securityagent#GitHubResourceCapabilities``."""

from typing_extensions import NotRequired, TypedDict


class GitHubResourceCapabilities(TypedDict, closed=True):
    leave_comments: NotRequired["bool"]
    """<p>Indicates whether the integration can leave comments on pull requests.</p>"""
    remediate_code: NotRequired["bool"]
    """<p>Indicates whether the integration can create code remediation pull requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GitHubResourceCapabilities) -> dict:
    out: dict = {}
    if "leave_comments" in value:
        out["leaveComments"] = value["leave_comments"]
    if "remediate_code" in value:
        out["remediateCode"] = value["remediate_code"]
    return out


def deserialize_json(data: dict) -> GitHubResourceCapabilities:
    out: GitHubResourceCapabilities = {}  # type: ignore[typeddict-item]
    if data.get("leaveComments") is not None:
        out["leave_comments"] = data["leaveComments"]
    if data.get("remediateCode") is not None:
        out["remediate_code"] = data["remediateCode"]
    return out
