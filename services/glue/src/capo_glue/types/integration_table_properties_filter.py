"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationTablePropertiesFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.integration_table_properties_filter_values
    import capo_glue.types.string128


class IntegrationTablePropertiesFilter(TypedDict, closed=True):
    name: NotRequired["capo_glue.types.string128.String128"]
    """<p>The name of the filter. Supported filter keys are <code>SourceArn</code>, <code>TargetArn</code>, <code>SourceTableName</code>, and <code>TargetTableName</code>.</p>"""
    values: NotRequired[
        "capo_glue.types.integration_table_properties_filter_values.IntegrationTablePropertiesFilterValues"
    ]
    """<p>A list of filter values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationTablePropertiesFilter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "values" in value:
        import capo_glue.types.integration_table_properties_filter_values

        out["Values"] = (
            capo_glue.types.integration_table_properties_filter_values.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IntegrationTablePropertiesFilter:
    out: IntegrationTablePropertiesFilter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Values") is not None:
        import capo_glue.types.integration_table_properties_filter_values

        out["values"] = (
            capo_glue.types.integration_table_properties_filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    return out
