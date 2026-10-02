"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityRuleResultsOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_table_config_options
    import capo_glue.types.nullable_boolean


class DataQualityRuleResultsOptions(TypedDict, closed=True):
    write_data_quality_rule_results_enabled: NotRequired[
        "capo_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Set to true to write data quality rule results.</p>"""
    catalog_table_config: NotRequired[
        "capo_glue.types.catalog_table_config_options.CatalogTableConfigOptions"
    ]
    """<p>The Glue Data Catalog table configuration for storing the rule results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityRuleResultsOptions) -> dict:
    out: dict = {}
    if "write_data_quality_rule_results_enabled" in value:
        out["WriteDataQualityRuleResultsEnabled"] = value[
            "write_data_quality_rule_results_enabled"
        ]
    if "catalog_table_config" in value:
        import capo_glue.types.catalog_table_config_options

        out["CatalogTableConfig"] = (
            capo_glue.types.catalog_table_config_options.serialize_aws_json_1_1(
                value["catalog_table_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityRuleResultsOptions:
    out: DataQualityRuleResultsOptions = {}  # type: ignore[typeddict-item]
    if data.get("WriteDataQualityRuleResultsEnabled") is not None:
        out["write_data_quality_rule_results_enabled"] = data[
            "WriteDataQualityRuleResultsEnabled"
        ]
    if data.get("CatalogTableConfig") is not None:
        import capo_glue.types.catalog_table_config_options

        out["catalog_table_config"] = (
            capo_glue.types.catalog_table_config_options.deserialize_aws_json_1_1(
                data["CatalogTableConfig"]
            )
        )
    return out
