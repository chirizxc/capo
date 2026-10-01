"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeLoggingOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.workspace_name


class DescribeLoggingOptionsRequest(TypedDict, closed=True):
    workspace_name: NotRequired["capo_iotsitewise.types.workspace_name.WorkspaceName"]
    """<p>The name of the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeLoggingOptionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeLoggingOptionsRequest:
    out: DescribeLoggingOptionsRequest = {}  # type: ignore[typeddict-item]
    return out
