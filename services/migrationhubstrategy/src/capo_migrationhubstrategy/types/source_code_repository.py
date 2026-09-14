"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#SourceCodeRepository``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.string


class SourceCodeRepository(TypedDict, closed=True):
    repository: NotRequired["capo_migrationhubstrategy.types.string.String"]
    """<p> The repository name for the source code. </p>"""
    branch: NotRequired["capo_migrationhubstrategy.types.string.String"]
    """<p> The branch of the source code. </p>"""
    version_control_type: NotRequired["capo_migrationhubstrategy.types.string.String"]
    """<p> The type of repository to use for the source code. </p>"""
    project_name: NotRequired["capo_migrationhubstrategy.types.string.String"]
    """<p>The name of the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceCodeRepository) -> dict:
    out: dict = {}
    if "repository" in value:
        out["repository"] = value["repository"]
    if "branch" in value:
        out["branch"] = value["branch"]
    if "version_control_type" in value:
        out["versionControlType"] = value["version_control_type"]
    if "project_name" in value:
        out["projectName"] = value["project_name"]
    return out


def deserialize_json(data: dict) -> SourceCodeRepository:
    out: SourceCodeRepository = {}  # type: ignore[typeddict-item]
    if data.get("repository") is not None:
        out["repository"] = data["repository"]
    if data.get("branch") is not None:
        out["branch"] = data["branch"]
    if data.get("versionControlType") is not None:
        out["version_control_type"] = data["versionControlType"]
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    return out
