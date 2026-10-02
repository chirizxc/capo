"""Generated from Smithy shape ``com.amazonaws.mq#DescribeSharedResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__string
    import capo_mq.types.max_results


class DescribeSharedResourcesRequest(TypedDict, closed=True):
    broker_id: "capo_mq.types.__string.__string"
    """<p>The unique ID that Amazon MQ generates for the broker.</p>"""
    max_results: NotRequired["capo_mq.types.max_results.MaxResults"]
    """<p>The maximum number of resources that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.</p>"""
    next_token: NotRequired["capo_mq.types.__string.__string"]
    """<p>The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSharedResourcesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeSharedResourcesRequest:
    out: DescribeSharedResourcesRequest = {}  # type: ignore[typeddict-item]
    return out
