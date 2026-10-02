"""Generated from Smithy shape ``com.amazonaws.glue#PutDataCatalogExportConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.export_encryption_configuration
    import capo_glue.types.export_setting


class PutDataCatalogExportConfigurationOutput(TypedDict, closed=True):
    export_setting: NotRequired["capo_glue.types.export_setting.ExportSetting"]
    """<p>The export setting for the data catalog.</p>"""
    encryption_configuration: NotRequired[
        "capo_glue.types.export_encryption_configuration.ExportEncryptionConfiguration"
    ]
    """<p>The encryption configuration for the exported data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutDataCatalogExportConfigurationOutput) -> dict:
    out: dict = {}
    if "export_setting" in value:
        import capo_glue.types.export_setting

        out["ExportSetting"] = capo_glue.types.export_setting.serialize_aws_json_1_1(
            value["export_setting"]
        )
    if "encryption_configuration" in value:
        import capo_glue.types.export_encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_glue.types.export_encryption_configuration.serialize_aws_json_1_1(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutDataCatalogExportConfigurationOutput:
    out: PutDataCatalogExportConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("ExportSetting") is not None:
        import capo_glue.types.export_setting

        out["export_setting"] = capo_glue.types.export_setting.deserialize_aws_json_1_1(
            data["ExportSetting"]
        )
    if data.get("EncryptionConfiguration") is not None:
        import capo_glue.types.export_encryption_configuration

        out["encryption_configuration"] = (
            capo_glue.types.export_encryption_configuration.deserialize_aws_json_1_1(
                data["EncryptionConfiguration"]
            )
        )
    return out
