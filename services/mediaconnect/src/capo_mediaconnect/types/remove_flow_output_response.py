"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RemoveFlowOutputResponse``."""

from typing_extensions import NotRequired, TypedDict


class RemoveFlowOutputResponse(TypedDict, closed=True):
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow that the output was removed from. </p>"""
    output_arn: NotRequired["str"]
    """<p> The ARN of the output that was removed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveFlowOutputResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "output_arn" in value:
        out["outputArn"] = value["output_arn"]
    return out


def deserialize_json(data: dict) -> RemoveFlowOutputResponse:
    out: RemoveFlowOutputResponse = {}  # type: ignore[typeddict-item]
    if data.get("flowArn") is not None:
        out["flow_arn"] = data["flowArn"]
    if data.get("outputArn") is not None:
        out["output_arn"] = data["outputArn"]
    return out
