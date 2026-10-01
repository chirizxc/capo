"""Generated from Smithy shape ``com.amazonaws.mq#ResourceShareError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__string


class ResourceShareError(TypedDict, closed=True):
    error_code: NotRequired["capo_mq.types.__string.__string"]
    """<p>The error code of the resource share.</p>"""
    resource_share_arn: NotRequired["capo_mq.types.__string.__string"]
    """<p>The ARN of the resource share.</p>"""
    status: NotRequired["capo_mq.types.__string.__string"]
    """<p>The status of the resource share.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareError) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "resource_share_arn" in value:
        out["resourceShareArn"] = value["resource_share_arn"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> ResourceShareError:
    out: ResourceShareError = {}  # type: ignore[typeddict-item]
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    if data.get("resourceShareArn") is not None:
        out["resource_share_arn"] = data["resourceShareArn"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    return out
