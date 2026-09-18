"""Generated from Smithy shape ``com.amazonaws.amplify#ProductionBranch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.branch_name
    import capo_amplify.types.last_deploy_time
    import capo_amplify.types.status
    import capo_amplify.types.thumbnail_url


class ProductionBranch(TypedDict, closed=True):
    last_deploy_time: NotRequired["capo_amplify.types.last_deploy_time.LastDeployTime"]
    """<p>The last deploy time of the production branch. </p>"""
    status: NotRequired["capo_amplify.types.status.Status"]
    """<p>The status of the production branch. </p>"""
    thumbnail_url: NotRequired["capo_amplify.types.thumbnail_url.ThumbnailUrl"]
    """<p>The thumbnail URL for the production branch. </p>"""
    branch_name: NotRequired["capo_amplify.types.branch_name.BranchName"]
    """<p>The branch name for the production branch. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProductionBranch) -> dict:
    out: dict = {}
    if "last_deploy_time" in value:
        import capo_amplify.types.last_deploy_time

        out["lastDeployTime"] = capo_amplify.types.last_deploy_time.serialize_json(
            value["last_deploy_time"]
        )
    if "status" in value:
        out["status"] = value["status"]
    if "thumbnail_url" in value:
        out["thumbnailUrl"] = value["thumbnail_url"]
    if "branch_name" in value:
        out["branchName"] = value["branch_name"]
    return out


def deserialize_json(data: dict) -> ProductionBranch:
    out: ProductionBranch = {}  # type: ignore[typeddict-item]
    if data.get("lastDeployTime") is not None:
        import capo_amplify.types.last_deploy_time

        out["last_deploy_time"] = capo_amplify.types.last_deploy_time.deserialize_json(
            data["lastDeployTime"]
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("thumbnailUrl") is not None:
        out["thumbnail_url"] = data["thumbnailUrl"]
    if data.get("branchName") is not None:
        out["branch_name"] = data["branchName"]
    return out
