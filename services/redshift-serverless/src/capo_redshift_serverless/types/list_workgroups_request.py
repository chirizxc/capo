"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListWorkgroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.owner_account


class ListWorkgroupsRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>If your initial ListWorkgroups operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following ListNamespaces operations, which returns results in the next page.</p>"""
    max_results: NotRequired["int"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>"""
    owner_account: NotRequired[
        "capo_redshift_serverless.types.owner_account.OwnerAccount"
    ]
    """<p>The owner Amazon Web Services account for the Amazon Redshift Serverless workgroup.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWorkgroupsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWorkgroupsRequest:
    out: ListWorkgroupsRequest = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("ownerAccount") is not None:
        out["owner_account"] = data["ownerAccount"]
    return out
