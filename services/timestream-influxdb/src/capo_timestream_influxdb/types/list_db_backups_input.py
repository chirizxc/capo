"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#ListDbBackupsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.db_resource_id
    import capo_timestream_influxdb.types.max_results
    import capo_timestream_influxdb.types.next_token


class ListDbBackupsInput(TypedDict, closed=True):
    db_resource_id: NotRequired[
        "capo_timestream_influxdb.types.db_resource_id.DbResourceId"
    ]
    """<p>The identifier of the DB instance or DB cluster to list backups for. If not specified, returns all backups in the account and region.</p>"""
    next_token: NotRequired["capo_timestream_influxdb.types.next_token.NextToken"]
    """<p>The pagination token. To resume pagination, provide the nextToken value as an argument of a subsequent API invocation.</p>"""
    max_results: NotRequired["capo_timestream_influxdb.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the output. If the total number of items available is more than the value specified, a nextToken is provided in the output. To resume pagination, provide the nextToken value as an argument of a subsequent API invocation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDbBackupsInput) -> dict:
    out: dict = {}
    if "db_resource_id" in value:
        out["dbResourceId"] = value["db_resource_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDbBackupsInput:
    out: ListDbBackupsInput = {}  # type: ignore[typeddict-item]
    if data.get("dbResourceId") is not None:
        out["db_resource_id"] = data["dbResourceId"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
