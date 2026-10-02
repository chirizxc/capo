"""Generated from Smithy shape ``com.amazonaws.glue#ListIntegrationTablePropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.integration_integer
    import capo_glue.types.integration_table_properties_filter_list
    import capo_glue.types.string4096


class ListIntegrationTablePropertiesRequest(TypedDict, closed=True):
    marker: NotRequired["capo_glue.types.string4096.String4096"]
    """<p>The pagination token for the next page of results. The initial value is <code>null</code>.</p>"""
    filters: NotRequired[
        "capo_glue.types.integration_table_properties_filter_list.IntegrationTablePropertiesFilterList"
    ]
    """<p>A list of filters. Supported filter keys are <code>SourceArn</code>, <code>TargetArn</code>, <code>SourceTableName</code>, and <code>TargetTableName</code>.</p>"""
    max_records: NotRequired["capo_glue.types.integration_integer.IntegrationInteger"]
    """<p>The maximum number of records to return in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListIntegrationTablePropertiesRequest) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "filters" in value:
        import capo_glue.types.integration_table_properties_filter_list

        out["Filters"] = (
            capo_glue.types.integration_table_properties_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListIntegrationTablePropertiesRequest:
    out: ListIntegrationTablePropertiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    if data.get("Filters") is not None:
        import capo_glue.types.integration_table_properties_filter_list

        out["filters"] = (
            capo_glue.types.integration_table_properties_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("MaxRecords") is not None:
        out["max_records"] = data["MaxRecords"]
    return out
