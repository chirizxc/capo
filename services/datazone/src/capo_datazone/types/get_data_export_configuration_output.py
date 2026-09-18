"""Generated from Smithy shape ``com.amazonaws.datazone#GetDataExportConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.configuration_status
    import capo_datazone.types.created_at
    import capo_datazone.types.encryption_configuration
    import capo_datazone.types.updated_at


class GetDataExportConfigurationOutput(TypedDict, closed=True):
    is_export_enabled: NotRequired["bool"]
    """<p>Specifies whether the export is enabled.</p>"""
    status: NotRequired["capo_datazone.types.configuration_status.ConfigurationStatus"]
    """<p>The status of the data export configuration.</p>"""
    encryption_configuration: NotRequired[
        "capo_datazone.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration as part of the data export configuration details.</p>"""
    s3_table_bucket_arn: NotRequired["str"]
    """<p>The Amazon S3 table bucket ARN as part of the data export configuration details.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which the data export configuration report was created.</p>"""
    updated_at: NotRequired["capo_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp at which the data export configuration report was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataExportConfigurationOutput) -> dict:
    out: dict = {}
    if "is_export_enabled" in value:
        out["isExportEnabled"] = value["is_export_enabled"]
    if "status" in value:
        import capo_datazone.types.configuration_status

        out["status"] = capo_datazone.types.configuration_status.serialize_json(
            value["status"]
        )
    if "encryption_configuration" in value:
        import capo_datazone.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_datazone.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "s3_table_bucket_arn" in value:
        out["s3TableBucketArn"] = value["s3_table_bucket_arn"]
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_datazone.types.updated_at

        out["updatedAt"] = capo_datazone.types.updated_at.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetDataExportConfigurationOutput:
    out: GetDataExportConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("isExportEnabled") is not None:
        out["is_export_enabled"] = data["isExportEnabled"]
    if data.get("status") is not None:
        import capo_datazone.types.configuration_status

        out["status"] = capo_datazone.types.configuration_status.deserialize_json(
            data["status"]
        )
    if data.get("encryptionConfiguration") is not None:
        import capo_datazone.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_datazone.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if data.get("s3TableBucketArn") is not None:
        out["s3_table_bucket_arn"] = data["s3TableBucketArn"]
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_datazone.types.updated_at

        out["updated_at"] = capo_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    return out
