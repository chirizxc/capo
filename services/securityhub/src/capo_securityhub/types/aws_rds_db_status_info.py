"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbStatusInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string


class AwsRdsDbStatusInfo(TypedDict, closed=True):
    status_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of status. For a read replica, the status type is read replication.</p>"""
    normal: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the read replica instance is operating normally.</p>"""
    status: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The status of the read replica instance.</p>"""
    message: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>If the read replica is currently in an error state, provides the error details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbStatusInfo) -> dict:
    out: dict = {}
    if "status_type" in value:
        out["StatusType"] = value["status_type"]
    if "normal" in value:
        out["Normal"] = value["normal"]
    if "status" in value:
        out["Status"] = value["status"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AwsRdsDbStatusInfo:
    out: AwsRdsDbStatusInfo = {}  # type: ignore[typeddict-item]
    if data.get("StatusType") is not None:
        out["status_type"] = data["StatusType"]
    if data.get("Normal") is not None:
        out["normal"] = data["Normal"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
