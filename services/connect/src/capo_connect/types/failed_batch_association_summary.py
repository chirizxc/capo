"""Generated from Smithy shape ``com.amazonaws.connect#FailedBatchAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.workspace_batch_error_message
    import capo_connect.types.workspace_error_code


class FailedBatchAssociationSummary(TypedDict, closed=True):
    resource_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the resource that failed to be associated.</p>"""
    error_code: NotRequired[
        "capo_connect.types.workspace_error_code.WorkspaceErrorCode"
    ]
    """<p>The error code indicating why the association failed.</p>"""
    error_message: NotRequired[
        "capo_connect.types.workspace_batch_error_message.WorkspaceBatchErrorMessage"
    ]
    """<p>An error message describing why the association failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedBatchAssociationSummary) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> FailedBatchAssociationSummary:
    out: FailedBatchAssociationSummary = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
