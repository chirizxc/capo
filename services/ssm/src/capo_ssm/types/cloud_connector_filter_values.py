"""Generated from Smithy shape ``com.amazonaws.ssm#CloudConnectorFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.cloud_connector_filter_value

CloudConnectorFilterValues: TypeAlias = list[
    "capo_ssm.types.cloud_connector_filter_value.CloudConnectorFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudConnectorFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CloudConnectorFilterValues:
    return [item for item in data if item is not None]
