"""Generated from Smithy shape ``com.amazonaws.configservice#ConnectorSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.connector_summary

ConnectorSummaries: TypeAlias = list[
    "capo_config_service.types.connector_summary.ConnectorSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorSummaries) -> list:
    import capo_config_service.types.connector_summary

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.connector_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectorSummaries:
    import capo_config_service.types.connector_summary

    out: ConnectorSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_config_service.types.connector_summary.deserialize_aws_json_1_1(item)
        )
    return out
