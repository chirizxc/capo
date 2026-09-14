"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListTracksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.pagination_token


class ListTracksRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_redshift_serverless.types.pagination_token.PaginationToken"
    ]
    """<p>If your initial <code>ListTracksRequest</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListTracksRequest</code> operations, which returns results in the next page.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTracksRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTracksRequest:
    out: ListTracksRequest = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
