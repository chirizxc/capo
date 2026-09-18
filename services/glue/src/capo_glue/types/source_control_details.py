"""Generated from Smithy shape ``com.amazonaws.glue#SourceControlDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.generic512_char_string
    import capo_glue.types.source_control_auth_strategy
    import capo_glue.types.source_control_provider


class SourceControlDetails(TypedDict, closed=True):
    provider: NotRequired[
        "capo_glue.types.source_control_provider.SourceControlProvider"
    ]
    """<p>The provider for the remote repository.</p>"""
    repository: NotRequired[
        "capo_glue.types.generic512_char_string.Generic512CharString"
    ]
    """<p>The name of the remote repository that contains the job artifacts.</p>"""
    owner: NotRequired["capo_glue.types.generic512_char_string.Generic512CharString"]
    """<p>The owner of the remote repository that contains the job artifacts.</p>"""
    branch: NotRequired["capo_glue.types.generic512_char_string.Generic512CharString"]
    """<p>An optional branch in the remote repository.</p>"""
    folder: NotRequired["capo_glue.types.generic512_char_string.Generic512CharString"]
    """<p>An optional folder in the remote repository.</p>"""
    last_commit_id: NotRequired[
        "capo_glue.types.generic512_char_string.Generic512CharString"
    ]
    """<p>The last commit ID for a commit in the remote repository.</p>"""
    auth_strategy: NotRequired[
        "capo_glue.types.source_control_auth_strategy.SourceControlAuthStrategy"
    ]
    """<p>The type of authentication, which can be an authentication token stored in Amazon Web Services Secrets Manager, or a personal access token.</p>"""
    auth_token: NotRequired[
        "capo_glue.types.generic512_char_string.Generic512CharString"
    ]
    """<p>The value of an authorization token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceControlDetails) -> dict:
    out: dict = {}
    if "provider" in value:
        import capo_glue.types.source_control_provider

        out["Provider"] = (
            capo_glue.types.source_control_provider.serialize_aws_json_1_1(
                value["provider"]
            )
        )
    if "repository" in value:
        out["Repository"] = value["repository"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "branch" in value:
        out["Branch"] = value["branch"]
    if "folder" in value:
        out["Folder"] = value["folder"]
    if "last_commit_id" in value:
        out["LastCommitId"] = value["last_commit_id"]
    if "auth_strategy" in value:
        import capo_glue.types.source_control_auth_strategy

        out["AuthStrategy"] = (
            capo_glue.types.source_control_auth_strategy.serialize_aws_json_1_1(
                value["auth_strategy"]
            )
        )
    if "auth_token" in value:
        out["AuthToken"] = value["auth_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceControlDetails:
    out: SourceControlDetails = {}  # type: ignore[typeddict-item]
    if data.get("Provider") is not None:
        import capo_glue.types.source_control_provider

        out["provider"] = (
            capo_glue.types.source_control_provider.deserialize_aws_json_1_1(
                data["Provider"]
            )
        )
    if data.get("Repository") is not None:
        out["repository"] = data["Repository"]
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("Branch") is not None:
        out["branch"] = data["Branch"]
    if data.get("Folder") is not None:
        out["folder"] = data["Folder"]
    if data.get("LastCommitId") is not None:
        out["last_commit_id"] = data["LastCommitId"]
    if data.get("AuthStrategy") is not None:
        import capo_glue.types.source_control_auth_strategy

        out["auth_strategy"] = (
            capo_glue.types.source_control_auth_strategy.deserialize_aws_json_1_1(
                data["AuthStrategy"]
            )
        )
    if data.get("AuthToken") is not None:
        out["auth_token"] = data["AuthToken"]
    return out
