"""Generated from Smithy shape ``com.amazonaws.datazone#GitPropertiesPatch``."""

from typing_extensions import NotRequired, TypedDict


class GitPropertiesPatch(TypedDict, closed=True):
    code_connection_arn: NotRequired["str"]
    """<p>The ARN of the CodeConnections connection used to connect to the Git repository.</p>"""
    default_branch: NotRequired["str"]
    """<p>The default branch of the Git repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GitPropertiesPatch) -> dict:
    out: dict = {}
    if "code_connection_arn" in value:
        out["codeConnectionArn"] = value["code_connection_arn"]
    if "default_branch" in value:
        out["defaultBranch"] = value["default_branch"]
    return out


def deserialize_json(data: dict) -> GitPropertiesPatch:
    out: GitPropertiesPatch = {}  # type: ignore[typeddict-item]
    if data.get("codeConnectionArn") is not None:
        out["code_connection_arn"] = data["codeConnectionArn"]
    if data.get("defaultBranch") is not None:
        out["default_branch"] = data["defaultBranch"]
    return out
