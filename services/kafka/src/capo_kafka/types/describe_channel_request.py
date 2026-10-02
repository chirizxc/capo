"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string


class DescribeChannelRequest(TypedDict, closed=True):
    channel_arn: "capo_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the channel.</p>"""
    cluster_arn: "capo_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeChannelRequest:
    out: DescribeChannelRequest = {}  # type: ignore[typeddict-item]
    return out
