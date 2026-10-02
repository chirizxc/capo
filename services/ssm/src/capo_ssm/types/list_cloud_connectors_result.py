"""Generated from Smithy shape ``com.amazonaws.ssm#ListCloudConnectorsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.cloud_connector_summary_list
    import capo_ssm.types.next_token


class ListCloudConnectorsResult(TypedDict, closed=True):
    cloud_connectors: NotRequired[
        "capo_ssm.types.cloud_connector_summary_list.CloudConnectorSummaryList"
    ]
    """<p>A list of cloud connector summary objects.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCloudConnectorsResult) -> dict:
    out: dict = {}
    if "cloud_connectors" in value:
        import capo_ssm.types.cloud_connector_summary_list

        out["CloudConnectors"] = (
            capo_ssm.types.cloud_connector_summary_list.serialize_aws_json_1_1(
                value["cloud_connectors"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCloudConnectorsResult:
    out: ListCloudConnectorsResult = {}  # type: ignore[typeddict-item]
    if data.get("CloudConnectors") is not None:
        import capo_ssm.types.cloud_connector_summary_list

        out["cloud_connectors"] = (
            capo_ssm.types.cloud_connector_summary_list.deserialize_aws_json_1_1(
                data["CloudConnectors"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
