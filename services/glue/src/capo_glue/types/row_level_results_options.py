"""Generated from Smithy shape ``com.amazonaws.glue#RowLevelResultsOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_table_config_options
    import capo_glue.types.nullable_integer
    import capo_glue.types.result_type_enum


class RowLevelResultsOptions(TypedDict, closed=True):
    max_rows_to_write: NotRequired["capo_glue.types.nullable_integer.NullableInteger"]
    """<p>The maximum number of rows to write in the results.</p>"""
    result_type: NotRequired["capo_glue.types.result_type_enum.ResultTypeEnum"]
    """<p>The result type to include in the row-level results output.</p>"""
    catalog_table_config: NotRequired[
        "capo_glue.types.catalog_table_config_options.CatalogTableConfigOptions"
    ]
    """<p>The Glue Data Catalog table configuration for storing the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RowLevelResultsOptions) -> dict:
    out: dict = {}
    if "max_rows_to_write" in value:
        out["MaxRowsToWrite"] = value["max_rows_to_write"]
    if "result_type" in value:
        import capo_glue.types.result_type_enum

        out["ResultType"] = capo_glue.types.result_type_enum.serialize_aws_json_1_1(
            value["result_type"]
        )
    if "catalog_table_config" in value:
        import capo_glue.types.catalog_table_config_options

        out["CatalogTableConfig"] = (
            capo_glue.types.catalog_table_config_options.serialize_aws_json_1_1(
                value["catalog_table_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RowLevelResultsOptions:
    out: RowLevelResultsOptions = {}  # type: ignore[typeddict-item]
    if data.get("MaxRowsToWrite") is not None:
        out["max_rows_to_write"] = data["MaxRowsToWrite"]
    if data.get("ResultType") is not None:
        import capo_glue.types.result_type_enum

        out["result_type"] = capo_glue.types.result_type_enum.deserialize_aws_json_1_1(
            data["ResultType"]
        )
    if data.get("CatalogTableConfig") is not None:
        import capo_glue.types.catalog_table_config_options

        out["catalog_table_config"] = (
            capo_glue.types.catalog_table_config_options.deserialize_aws_json_1_1(
                data["CatalogTableConfig"]
            )
        )
    return out
