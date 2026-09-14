"""Generated from Smithy shape ``com.amazonaws.mgn#JobLogEventData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.ec2_instance_id
    import capo_mgn.types.large_bounded_string
    import capo_mgn.types.source_server_id
    import capo_mgn.types.strictly_positive_integer


class JobLogEventData(TypedDict, closed=True):
    source_server_id: NotRequired["capo_mgn.types.source_server_id.SourceServerID"]
    """<p>Job Event Source Server ID.</p>"""
    conversion_server_id: NotRequired["capo_mgn.types.ec2_instance_id.EC2InstanceID"]
    """<p>Job Event conversion Server ID.</p>"""
    target_instance_id: NotRequired["capo_mgn.types.ec2_instance_id.EC2InstanceID"]
    """<p>Job Event Target instance ID.</p>"""
    raw_error: NotRequired["capo_mgn.types.large_bounded_string.LargeBoundedString"]
    """<p>Job error.</p>"""
    attempt_count: NotRequired[
        "capo_mgn.types.strictly_positive_integer.StrictlyPositiveInteger"
    ]
    """<p>Retries for this operation.</p>"""
    max_attempts_count: NotRequired[
        "capo_mgn.types.strictly_positive_integer.StrictlyPositiveInteger"
    ]
    """<p>The maximum number of retries that will be attempted if this operation failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobLogEventData) -> dict:
    out: dict = {}
    if "source_server_id" in value:
        out["sourceServerID"] = value["source_server_id"]
    if "conversion_server_id" in value:
        out["conversionServerID"] = value["conversion_server_id"]
    if "target_instance_id" in value:
        out["targetInstanceID"] = value["target_instance_id"]
    if "raw_error" in value:
        out["rawError"] = value["raw_error"]
    if "attempt_count" in value:
        out["attemptCount"] = value["attempt_count"]
    if "max_attempts_count" in value:
        out["maxAttemptsCount"] = value["max_attempts_count"]
    return out


def deserialize_json(data: dict) -> JobLogEventData:
    out: JobLogEventData = {}  # type: ignore[typeddict-item]
    if data.get("sourceServerID") is not None:
        out["source_server_id"] = data["sourceServerID"]
    if data.get("conversionServerID") is not None:
        out["conversion_server_id"] = data["conversionServerID"]
    if data.get("targetInstanceID") is not None:
        out["target_instance_id"] = data["targetInstanceID"]
    if data.get("rawError") is not None:
        out["raw_error"] = data["rawError"]
    if data.get("attemptCount") is not None:
        out["attempt_count"] = data["attemptCount"]
    if data.get("maxAttemptsCount") is not None:
        out["max_attempts_count"] = data["maxAttemptsCount"]
    return out
