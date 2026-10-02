"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationTablePropertiesFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.integration_table_properties_filter

IntegrationTablePropertiesFilterList: TypeAlias = list[
    "capo_glue.types.integration_table_properties_filter.IntegrationTablePropertiesFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationTablePropertiesFilterList) -> list:
    import capo_glue.types.integration_table_properties_filter

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.integration_table_properties_filter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IntegrationTablePropertiesFilterList:
    import capo_glue.types.integration_table_properties_filter

    out: IntegrationTablePropertiesFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_glue.types.integration_table_properties_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
