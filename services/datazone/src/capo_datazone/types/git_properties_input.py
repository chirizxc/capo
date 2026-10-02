"""Generated from Smithy shape ``com.amazonaws.datazone#GitPropertiesInput``."""

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError


class GitPropertiesInput(TypedDict, closed=True):
    code_connection_arn: "str"
    """<p>The ARN of the CodeConnections connection used to connect to the Git repository.</p>"""
    repository_id: "str"
    """<p>The ID of the Git repository. This is the owner and repository name, for example, owner/repo-name.</p>"""
    default_branch: "str"
    """<p>The default branch of the Git repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GitPropertiesInput) -> dict:
    out: dict = {}
    out["codeConnectionArn"] = value["code_connection_arn"]
    out["repositoryId"] = value["repository_id"]
    out["defaultBranch"] = value["default_branch"]
    return out


def deserialize_json(data: dict) -> GitPropertiesInput:
    out: GitPropertiesInput = {}  # type: ignore[typeddict-item]
    if data.get("codeConnectionArn") is not None:
        out["code_connection_arn"] = data["codeConnectionArn"]
    else:
        raise DeserializationError("GitPropertiesInput.code_connection_arn required")
    if data.get("repositoryId") is not None:
        out["repository_id"] = data["repositoryId"]
    else:
        raise DeserializationError("GitPropertiesInput.repository_id required")
    if data.get("defaultBranch") is not None:
        out["default_branch"] = data["defaultBranch"]
    else:
        raise DeserializationError("GitPropertiesInput.default_branch required")
    return out
