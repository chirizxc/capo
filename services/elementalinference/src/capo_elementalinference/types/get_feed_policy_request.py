"""Generated from Smithy shape ``com.amazonaws.elementalinference#GetFeedPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.feed_id


class GetFeedPolicyRequest(TypedDict, closed=True):
    id: "capo_elementalinference.types.feed_id.FeedId"
    """<p>The ID of the feed whose policy you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFeedPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFeedPolicyRequest:
    out: GetFeedPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
