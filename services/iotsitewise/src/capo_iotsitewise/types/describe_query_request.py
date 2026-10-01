"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeQueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.query_id
    import capo_iotsitewise.types.workspace_name


class DescribeQueryRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace associated with the query.</p>"""
    query_id: "capo_iotsitewise.types.query_id.QueryId"
    """<p>The unique identifier for the query execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeQueryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeQueryRequest:
    out: DescribeQueryRequest = {}  # type: ignore[typeddict-item]
    return out
