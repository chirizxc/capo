"""Generated from Smithy shape ``com.amazonaws.ssm#CloudConnectorSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.cloud_connector_summary

CloudConnectorSummaryList: TypeAlias = list[
    "capo_ssm.types.cloud_connector_summary.CloudConnectorSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudConnectorSummaryList) -> list:
    import capo_ssm.types.cloud_connector_summary

    out: list = []
    for item in value:
        out.append(capo_ssm.types.cloud_connector_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CloudConnectorSummaryList:
    import capo_ssm.types.cloud_connector_summary

    out: CloudConnectorSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ssm.types.cloud_connector_summary.deserialize_aws_json_1_1(item)
        )
    return out
