"""Generated from Smithy shape ``com.amazonaws.kafka#ListChannelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.max_results


class ListChannelsRequest(TypedDict, closed=True):
    cluster_arn: "capo_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""
    max_results: NotRequired["capo_kafka.types.max_results.MaxResults"]
    """<p>Maximum number of channels to return in a single response.</p>"""
    next_token: NotRequired["capo_kafka.types.__string.__string"]
    """<p>If the response of ListChannels is truncated, it returns a nextToken in the response. This nextToken should be sent in the subsequent request to ListChannels.</p>"""
    topic_name_filter: NotRequired["capo_kafka.types.__string.__string"]
    """<p>Filters results to channels whose topic name matches the specified value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListChannelsRequest:
    out: ListChannelsRequest = {}  # type: ignore[typeddict-item]
    return out
