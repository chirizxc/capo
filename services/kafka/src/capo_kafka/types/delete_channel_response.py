"""Generated from Smithy shape ``com.amazonaws.kafka#DeleteChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string


class DeleteChannelResponse(TypedDict, closed=True):
    channel_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the channel.</p>"""
    cluster_operation_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the cluster operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteChannelResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["channelArn"] = value["channel_arn"]
    if "cluster_operation_arn" in value:
        out["clusterOperationArn"] = value["cluster_operation_arn"]
    return out


def deserialize_json(data: dict) -> DeleteChannelResponse:
    out: DeleteChannelResponse = {}  # type: ignore[typeddict-item]
    if data.get("channelArn") is not None:
        out["channel_arn"] = data["channelArn"]
    if data.get("clusterOperationArn") is not None:
        out["cluster_operation_arn"] = data["clusterOperationArn"]
    return out
