"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeSearchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.search_id
    import capo_iotsitewise.types.workspace_name


class DescribeSearchRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace the search belongs to.</p>"""
    search_id: "capo_iotsitewise.types.search_id.SearchId"
    """<p>The identifier of the search to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSearchRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeSearchRequest:
    out: DescribeSearchRequest = {}  # type: ignore[typeddict-item]
    return out
