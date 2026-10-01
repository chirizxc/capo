"""Generated from Smithy shape ``com.amazonaws.inspector2#AwsConfigConnectorArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.aws_config_connector_arn

AwsConfigConnectorArnList: TypeAlias = list[
    "capo_inspector2.types.aws_config_connector_arn.AwsConfigConnectorArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsConfigConnectorArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> AwsConfigConnectorArnList:
    return [item for item in data if item is not None]
