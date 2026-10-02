"""Generated from Smithy shape ``com.amazonaws.configservice#ConnectorFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.connector_filter

ConnectorFilterList: TypeAlias = list[
    "capo_config_service.types.connector_filter.ConnectorFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorFilterList) -> list:
    import capo_config_service.types.connector_filter

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.connector_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectorFilterList:
    import capo_config_service.types.connector_filter

    out: ConnectorFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_config_service.types.connector_filter.deserialize_aws_json_1_1(item)
        )
    return out
