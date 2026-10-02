"""Generated from Smithy shape ``com.amazonaws.glue#ListIntegrationTablePropertiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.integration_table_properties_list
    import capo_glue.types.string4096


class ListIntegrationTablePropertiesResponse(TypedDict, closed=True):
    integration_table_properties_list: NotRequired[
        "capo_glue.types.integration_table_properties_list.IntegrationTablePropertiesList"
    ]
    """<p>A list of integration table properties meeting the filter criteria.</p>"""
    marker: NotRequired["capo_glue.types.string4096.String4096"]
    """<p>The pagination token for the next page. Returns <code>null</code> if there are no more results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListIntegrationTablePropertiesResponse) -> dict:
    out: dict = {}
    if "integration_table_properties_list" in value:
        import capo_glue.types.integration_table_properties_list

        out["IntegrationTablePropertiesList"] = (
            capo_glue.types.integration_table_properties_list.serialize_aws_json_1_1(
                value["integration_table_properties_list"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListIntegrationTablePropertiesResponse:
    out: ListIntegrationTablePropertiesResponse = {}  # type: ignore[typeddict-item]
    if data.get("IntegrationTablePropertiesList") is not None:
        import capo_glue.types.integration_table_properties_list

        out["integration_table_properties_list"] = (
            capo_glue.types.integration_table_properties_list.deserialize_aws_json_1_1(
                data["IntegrationTablePropertiesList"]
            )
        )
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    return out
