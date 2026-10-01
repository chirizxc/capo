"""Generated from Smithy shape ``com.amazonaws.ssm#CloudConnectorFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.cloud_connector_filter

CloudConnectorFilterList: TypeAlias = list[
    "capo_ssm.types.cloud_connector_filter.CloudConnectorFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudConnectorFilterList) -> list:
    import capo_ssm.types.cloud_connector_filter

    out: list = []
    for item in value:
        out.append(capo_ssm.types.cloud_connector_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CloudConnectorFilterList:
    import capo_ssm.types.cloud_connector_filter

    out: CloudConnectorFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.cloud_connector_filter.deserialize_aws_json_1_1(item))
    return out
