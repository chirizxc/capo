"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.client_request_token
    import capo_fsx.types.snapshot_id
    import capo_fsx.types.snapshot_name


class UpdateSnapshotRequest(TypedDict, closed=True):
    client_request_token: NotRequired[
        "capo_fsx.types.client_request_token.ClientRequestToken"
    ]
    name: NotRequired["capo_fsx.types.snapshot_name.SnapshotName"]
    """<p>The name of the snapshot to update.</p>"""
    snapshot_id: NotRequired["capo_fsx.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot that you want to update, in the format <code>fsvolsnap-0123456789abcdef0</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSnapshotRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "name" in value:
        out["Name"] = value["name"]
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSnapshotRequest:
    out: UpdateSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("SnapshotId") is not None:
        out["snapshot_id"] = data["SnapshotId"]
    return out
