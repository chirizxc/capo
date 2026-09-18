"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RemoveFlowMediaStreamResponse``."""

from typing_extensions import NotRequired, TypedDict


class RemoveFlowMediaStreamResponse(TypedDict, closed=True):
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow that was updated.</p>"""
    media_stream_name: NotRequired["str"]
    """<p> The name of the media stream that was removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveFlowMediaStreamResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "media_stream_name" in value:
        out["mediaStreamName"] = value["media_stream_name"]
    return out


def deserialize_json(data: dict) -> RemoveFlowMediaStreamResponse:
    out: RemoveFlowMediaStreamResponse = {}  # type: ignore[typeddict-item]
    if data.get("flowArn") is not None:
        out["flow_arn"] = data["flowArn"]
    if data.get("mediaStreamName") is not None:
        out["media_stream_name"] = data["mediaStreamName"]
    return out
