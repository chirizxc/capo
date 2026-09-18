"""Generated from Smithy shape ``com.amazonaws.neptunedata#MlResourceDefinition``."""

from typing_extensions import NotRequired, TypedDict


class MlResourceDefinition(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The resource name.</p>"""
    arn: NotRequired["str"]
    """<p>The resource ARN.</p>"""
    status: NotRequired["str"]
    """<p>The resource status.</p>"""
    output_location: NotRequired["str"]
    """<p>The output location.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The failure reason, in case of a failure.</p>"""
    cloudwatch_log_url: NotRequired["str"]
    """<p>The CloudWatch log URL for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MlResourceDefinition) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "output_location" in value:
        out["outputLocation"] = value["output_location"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "cloudwatch_log_url" in value:
        out["cloudwatchLogUrl"] = value["cloudwatch_log_url"]
    return out


def deserialize_json(data: dict) -> MlResourceDefinition:
    out: MlResourceDefinition = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("outputLocation") is not None:
        out["output_location"] = data["outputLocation"]
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    if data.get("cloudwatchLogUrl") is not None:
        out["cloudwatch_log_url"] = data["cloudwatchLogUrl"]
    return out
