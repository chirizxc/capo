"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CancelQueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.query_id
    import capo_iotsitewise.types.workspace_name


class CancelQueryRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace associated with the query.</p>"""
    query_id: "capo_iotsitewise.types.query_id.QueryId"
    """<p>The unique identifier for the query execution to cancel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelQueryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelQueryRequest:
    out: CancelQueryRequest = {}  # type: ignore[typeddict-item]
    return out
