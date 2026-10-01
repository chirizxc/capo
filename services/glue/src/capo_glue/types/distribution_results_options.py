"""Generated from Smithy shape ``com.amazonaws.glue#DistributionResultsOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_table_config_options
    import capo_glue.types.nullable_boolean


class DistributionResultsOptions(TypedDict, closed=True):
    write_distribution_results_enabled: NotRequired[
        "capo_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Set to true to write distribution results.</p>"""
    catalog_table_config: NotRequired[
        "capo_glue.types.catalog_table_config_options.CatalogTableConfigOptions"
    ]
    """<p>The Glue Data Catalog table configuration for storing the distribution results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DistributionResultsOptions) -> dict:
    out: dict = {}
    if "write_distribution_results_enabled" in value:
        out["WriteDistributionResultsEnabled"] = value[
            "write_distribution_results_enabled"
        ]
    if "catalog_table_config" in value:
        import capo_glue.types.catalog_table_config_options

        out["CatalogTableConfig"] = (
            capo_glue.types.catalog_table_config_options.serialize_aws_json_1_1(
                value["catalog_table_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DistributionResultsOptions:
    out: DistributionResultsOptions = {}  # type: ignore[typeddict-item]
    if data.get("WriteDistributionResultsEnabled") is not None:
        out["write_distribution_results_enabled"] = data[
            "WriteDistributionResultsEnabled"
        ]
    if data.get("CatalogTableConfig") is not None:
        import capo_glue.types.catalog_table_config_options

        out["catalog_table_config"] = (
            capo_glue.types.catalog_table_config_options.deserialize_aws_json_1_1(
                data["CatalogTableConfig"]
            )
        )
    return out
