"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RemoveFlowSourceResponse``."""

from typing_extensions import NotRequired, TypedDict


class RemoveFlowSourceResponse(TypedDict, closed=True):
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow that the source was removed from. </p>"""
    source_arn: NotRequired["str"]
    """<p> The ARN of the source that was removed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveFlowSourceResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "source_arn" in value:
        out["sourceArn"] = value["source_arn"]
    return out


def deserialize_json(data: dict) -> RemoveFlowSourceResponse:
    out: RemoveFlowSourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("flowArn") is not None:
        out["flow_arn"] = data["flowArn"]
    if data.get("sourceArn") is not None:
        out["source_arn"] = data["sourceArn"]
    return out
