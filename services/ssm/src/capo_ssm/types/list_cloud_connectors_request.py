"""Generated from Smithy shape ``com.amazonaws.ssm#ListCloudConnectorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.cloud_connector_filter_list
    import capo_ssm.types.cloud_connector_max_results
    import capo_ssm.types.next_token


class ListCloudConnectorsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_ssm.types.cloud_connector_max_results.CloudConnectorMaxResults"
    ]
    """<p>The maximum number of items to return for this call.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    filters: NotRequired[
        "capo_ssm.types.cloud_connector_filter_list.CloudConnectorFilterList"
    ]
    """<p>One or more filters to limit the cloud connectors returned in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCloudConnectorsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import capo_ssm.types.cloud_connector_filter_list

        out["Filters"] = (
            capo_ssm.types.cloud_connector_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCloudConnectorsRequest:
    out: ListCloudConnectorsRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Filters") is not None:
        import capo_ssm.types.cloud_connector_filter_list

        out["filters"] = (
            capo_ssm.types.cloud_connector_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    return out
