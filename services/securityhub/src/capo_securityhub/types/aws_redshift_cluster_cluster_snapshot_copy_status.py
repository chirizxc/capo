"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterClusterSnapshotCopyStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsRedshiftClusterClusterSnapshotCopyStatus(TypedDict, closed=True):
    destination_region: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The destination Region that snapshots are automatically copied to when cross-Region snapshot copy is enabled.</p>"""
    manual_snapshot_retention_period: NotRequired[
        "capo_securityhub.types.integer.Integer"
    ]
    """<p>The number of days that manual snapshots are retained in the destination Region after they are copied from a source Region.</p> <p>If the value is <code>-1</code>, then the manual snapshot is retained indefinitely.</p> <p>Valid values: Either <code>-1</code> or an integer between 1 and 3,653</p>"""
    retention_period: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of days to retain automated snapshots in the destination Region after they are copied from a source Region.</p>"""
    snapshot_copy_grant_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the snapshot copy grant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterClusterSnapshotCopyStatus) -> dict:
    out: dict = {}
    if "destination_region" in value:
        out["DestinationRegion"] = value["destination_region"]
    if "manual_snapshot_retention_period" in value:
        out["ManualSnapshotRetentionPeriod"] = value["manual_snapshot_retention_period"]
    if "retention_period" in value:
        out["RetentionPeriod"] = value["retention_period"]
    if "snapshot_copy_grant_name" in value:
        out["SnapshotCopyGrantName"] = value["snapshot_copy_grant_name"]
    return out


def deserialize_json(data: dict) -> AwsRedshiftClusterClusterSnapshotCopyStatus:
    out: AwsRedshiftClusterClusterSnapshotCopyStatus = {}  # type: ignore[typeddict-item]
    if data.get("DestinationRegion") is not None:
        out["destination_region"] = data["DestinationRegion"]
    if data.get("ManualSnapshotRetentionPeriod") is not None:
        out["manual_snapshot_retention_period"] = data["ManualSnapshotRetentionPeriod"]
    if data.get("RetentionPeriod") is not None:
        out["retention_period"] = data["RetentionPeriod"]
    if data.get("SnapshotCopyGrantName") is not None:
        out["snapshot_copy_grant_name"] = data["SnapshotCopyGrantName"]
    return out
