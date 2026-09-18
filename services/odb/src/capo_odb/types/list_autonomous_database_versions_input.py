"""Generated from Smithy shape ``com.amazonaws.odb#ListAutonomousDatabaseVersionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.db_workload


class ListAutonomousDatabaseVersionsInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>"""
    next_token: NotRequired["str"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    db_workload: NotRequired["capo_odb.types.db_workload.DbWorkload"]
    """<p>The intended use of the Autonomous Database to return versions for, such as transaction processing, data warehouse, JSON database, or APEX.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutonomousDatabaseVersionsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "db_workload" in value:
        import capo_odb.types.db_workload

        out["dbWorkload"] = capo_odb.types.db_workload.serialize_aws_json_1_0(
            value["db_workload"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutonomousDatabaseVersionsInput:
    out: ListAutonomousDatabaseVersionsInput = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("dbWorkload") is not None:
        import capo_odb.types.db_workload

        out["db_workload"] = capo_odb.types.db_workload.deserialize_aws_json_1_0(
            data["dbWorkload"]
        )
    return out
