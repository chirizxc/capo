"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationTablePropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.integration_table_properties

IntegrationTablePropertiesList: TypeAlias = list[
    "capo_glue.types.integration_table_properties.IntegrationTableProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationTablePropertiesList) -> list:
    import capo_glue.types.integration_table_properties

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.integration_table_properties.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IntegrationTablePropertiesList:
    import capo_glue.types.integration_table_properties

    out: IntegrationTablePropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_glue.types.integration_table_properties.deserialize_aws_json_1_1(item)
        )
    return out
