"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#SnapshotCopyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.kms_key_id
    import capo_redshift_serverless.types.namespace_name


class SnapshotCopyConfiguration(TypedDict, closed=True):
    snapshot_copy_configuration_id: NotRequired["str"]
    """<p>The ID of the snapshot copy configuration object.</p>"""
    snapshot_copy_configuration_arn: NotRequired["str"]
    """<p>The ARN of the snapshot copy configuration object.</p>"""
    namespace_name: NotRequired[
        "capo_redshift_serverless.types.namespace_name.NamespaceName"
    ]
    """<p>The name of the namespace to copy snapshots from in the source Amazon Web Services Region.</p>"""
    destination_region: NotRequired["str"]
    """<p>The destination Amazon Web Services Region to copy snapshots to.</p>"""
    snapshot_retention_period: NotRequired["int"]
    """<p>The retention period of snapshots that are copied to the destination Amazon Web Services Region.</p>"""
    destination_kms_key_id: NotRequired[
        "capo_redshift_serverless.types.kms_key_id.KmsKeyId"
    ]
    """<p>The ID of the KMS key to use to encrypt your snapshots in the destination Amazon Web Services Region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotCopyConfiguration) -> dict:
    out: dict = {}
    if "snapshot_copy_configuration_id" in value:
        out["snapshotCopyConfigurationId"] = value["snapshot_copy_configuration_id"]
    if "snapshot_copy_configuration_arn" in value:
        out["snapshotCopyConfigurationArn"] = value["snapshot_copy_configuration_arn"]
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    if "destination_region" in value:
        out["destinationRegion"] = value["destination_region"]
    if "snapshot_retention_period" in value:
        out["snapshotRetentionPeriod"] = value["snapshot_retention_period"]
    if "destination_kms_key_id" in value:
        out["destinationKmsKeyId"] = value["destination_kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SnapshotCopyConfiguration:
    out: SnapshotCopyConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("snapshotCopyConfigurationId") is not None:
        out["snapshot_copy_configuration_id"] = data["snapshotCopyConfigurationId"]
    if data.get("snapshotCopyConfigurationArn") is not None:
        out["snapshot_copy_configuration_arn"] = data["snapshotCopyConfigurationArn"]
    if data.get("namespaceName") is not None:
        out["namespace_name"] = data["namespaceName"]
    if data.get("destinationRegion") is not None:
        out["destination_region"] = data["destinationRegion"]
    if data.get("snapshotRetentionPeriod") is not None:
        out["snapshot_retention_period"] = data["snapshotRetentionPeriod"]
    if data.get("destinationKmsKeyId") is not None:
        out["destination_kms_key_id"] = data["destinationKmsKeyId"]
    return out
