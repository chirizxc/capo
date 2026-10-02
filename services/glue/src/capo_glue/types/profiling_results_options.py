"""Generated from Smithy shape ``com.amazonaws.glue#ProfilingResultsOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_table_config_options
    import capo_glue.types.distribution_results_options
    import capo_glue.types.nullable_boolean


class ProfilingResultsOptions(TypedDict, closed=True):
    write_profiling_results_enabled: NotRequired[
        "capo_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Set to true to write profiling results.</p>"""
    catalog_table_config: NotRequired[
        "capo_glue.types.catalog_table_config_options.CatalogTableConfigOptions"
    ]
    """<p>The Glue Data Catalog table configuration for storing the profiling results.</p>"""
    distribution_results: NotRequired[
        "capo_glue.types.distribution_results_options.DistributionResultsOptions"
    ]
    """<p>The configuration for writing distribution results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProfilingResultsOptions) -> dict:
    out: dict = {}
    if "write_profiling_results_enabled" in value:
        out["WriteProfilingResultsEnabled"] = value["write_profiling_results_enabled"]
    if "catalog_table_config" in value:
        import capo_glue.types.catalog_table_config_options

        out["CatalogTableConfig"] = (
            capo_glue.types.catalog_table_config_options.serialize_aws_json_1_1(
                value["catalog_table_config"]
            )
        )
    if "distribution_results" in value:
        import capo_glue.types.distribution_results_options

        out["DistributionResults"] = (
            capo_glue.types.distribution_results_options.serialize_aws_json_1_1(
                value["distribution_results"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProfilingResultsOptions:
    out: ProfilingResultsOptions = {}  # type: ignore[typeddict-item]
    if data.get("WriteProfilingResultsEnabled") is not None:
        out["write_profiling_results_enabled"] = data["WriteProfilingResultsEnabled"]
    if data.get("CatalogTableConfig") is not None:
        import capo_glue.types.catalog_table_config_options

        out["catalog_table_config"] = (
            capo_glue.types.catalog_table_config_options.deserialize_aws_json_1_1(
                data["CatalogTableConfig"]
            )
        )
    if data.get("DistributionResults") is not None:
        import capo_glue.types.distribution_results_options

        out["distribution_results"] = (
            capo_glue.types.distribution_results_options.deserialize_aws_json_1_1(
                data["DistributionResults"]
            )
        )
    return out
