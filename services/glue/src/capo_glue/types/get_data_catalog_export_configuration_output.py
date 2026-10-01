"""Generated from Smithy shape ``com.amazonaws.glue#GetDataCatalogExportConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.created_at
    import capo_glue.types.export_encryption_configuration
    import capo_glue.types.export_setting
    import capo_glue.types.export_status
    import capo_glue.types.s3_table_bucket_arn
    import capo_glue.types.updated_at


class GetDataCatalogExportConfigurationOutput(TypedDict, closed=True):
    export_setting: NotRequired["capo_glue.types.export_setting.ExportSetting"]
    """<p>The export setting for the data catalog. Valid values are <code>ENABLED</code> and <code>DISABLED</code>.</p>"""
    status: NotRequired["capo_glue.types.export_status.ExportStatus"]
    """<p>The current status of the export. Valid values are <code>ENABLING</code>, <code>ENABLED</code>, <code>DISABLING</code>, <code>DISABLED</code>, and <code>FAILED</code>.</p>"""
    encryption_configuration: NotRequired[
        "capo_glue.types.export_encryption_configuration.ExportEncryptionConfiguration"
    ]
    """<p>The encryption configuration for the exported data.</p>"""
    s3_table_bucket_arn: NotRequired[
        "capo_glue.types.s3_table_bucket_arn.S3TableBucketArn"
    ]
    """<p>The ARN of the S3 Tables bucket where catalog metadata is exported.</p>"""
    created_at: NotRequired["capo_glue.types.created_at.CreatedAt"]
    """<p>The timestamp at which the export configuration was created.</p>"""
    updated_at: NotRequired["capo_glue.types.updated_at.UpdatedAt"]
    """<p>The timestamp at which the export configuration was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataCatalogExportConfigurationOutput) -> dict:
    out: dict = {}
    if "export_setting" in value:
        import capo_glue.types.export_setting

        out["ExportSetting"] = capo_glue.types.export_setting.serialize_aws_json_1_1(
            value["export_setting"]
        )
    if "status" in value:
        import capo_glue.types.export_status

        out["Status"] = capo_glue.types.export_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "encryption_configuration" in value:
        import capo_glue.types.export_encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_glue.types.export_encryption_configuration.serialize_aws_json_1_1(
                value["encryption_configuration"]
            )
        )
    if "s3_table_bucket_arn" in value:
        out["S3TableBucketArn"] = value["s3_table_bucket_arn"]
    if "created_at" in value:
        import capo_glue.types.created_at

        out["CreatedAt"] = capo_glue.types.created_at.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_glue.types.updated_at

        out["UpdatedAt"] = capo_glue.types.updated_at.serialize_aws_json_1_1(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataCatalogExportConfigurationOutput:
    out: GetDataCatalogExportConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("ExportSetting") is not None:
        import capo_glue.types.export_setting

        out["export_setting"] = capo_glue.types.export_setting.deserialize_aws_json_1_1(
            data["ExportSetting"]
        )
    if data.get("Status") is not None:
        import capo_glue.types.export_status

        out["status"] = capo_glue.types.export_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("EncryptionConfiguration") is not None:
        import capo_glue.types.export_encryption_configuration

        out["encryption_configuration"] = (
            capo_glue.types.export_encryption_configuration.deserialize_aws_json_1_1(
                data["EncryptionConfiguration"]
            )
        )
    if data.get("S3TableBucketArn") is not None:
        out["s3_table_bucket_arn"] = data["S3TableBucketArn"]
    if data.get("CreatedAt") is not None:
        import capo_glue.types.created_at

        out["created_at"] = capo_glue.types.created_at.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_glue.types.updated_at

        out["updated_at"] = capo_glue.types.updated_at.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    return out
