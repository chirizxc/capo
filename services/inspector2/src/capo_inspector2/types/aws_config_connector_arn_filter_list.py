"""Generated from Smithy shape ``com.amazonaws.inspector2#AwsConfigConnectorArnFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.aws_config_connector_arn_filter

AwsConfigConnectorArnFilterList: TypeAlias = list[
    "capo_inspector2.types.aws_config_connector_arn_filter.AwsConfigConnectorArnFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsConfigConnectorArnFilterList) -> list:
    import capo_inspector2.types.aws_config_connector_arn_filter

    out: list = []
    for item in value:
        out.append(
            capo_inspector2.types.aws_config_connector_arn_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsConfigConnectorArnFilterList:
    import capo_inspector2.types.aws_config_connector_arn_filter

    out: AwsConfigConnectorArnFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_inspector2.types.aws_config_connector_arn_filter.deserialize_json(item)
        )
    return out
