"""Generated from Smithy shape ``com.amazonaws.drs#JobLogEventData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.conversion_properties
    import capo_drs.types.ec2_instance_id
    import capo_drs.types.event_resource_data
    import capo_drs.types.job_event_attempt_count
    import capo_drs.types.large_bounded_string
    import capo_drs.types.source_server_id


class JobLogEventData(TypedDict, closed=True):
    source_server_id: NotRequired["capo_drs.types.source_server_id.SourceServerID"]
    """<p>The ID of a Source Server.</p>"""
    conversion_server_id: NotRequired["capo_drs.types.ec2_instance_id.EC2InstanceID"]
    """<p>The ID of a conversion server.</p>"""
    target_instance_id: NotRequired["capo_drs.types.ec2_instance_id.EC2InstanceID"]
    """<p>The ID of a Recovery Instance.</p>"""
    raw_error: NotRequired["capo_drs.types.large_bounded_string.LargeBoundedString"]
    """<p>A string representing a job error.</p>"""
    conversion_properties: NotRequired[
        "capo_drs.types.conversion_properties.ConversionProperties"
    ]
    """<p>Properties of a conversion job</p>"""
    event_resource_data: NotRequired[
        "capo_drs.types.event_resource_data.EventResourceData"
    ]
    """<p>Properties of resource related to a job event.</p>"""
    attempt_count: "capo_drs.types.job_event_attempt_count.JobEventAttemptCount"
    """<p>Retries for this operation.</p>"""
    max_attempts_count: "capo_drs.types.job_event_attempt_count.JobEventAttemptCount"
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
    if "conversion_properties" in value:
        import capo_drs.types.conversion_properties

        out["conversionProperties"] = (
            capo_drs.types.conversion_properties.serialize_json(
                value["conversion_properties"]
            )
        )
    if "event_resource_data" in value:
        import capo_drs.types.event_resource_data

        out["eventResourceData"] = capo_drs.types.event_resource_data.serialize_json(
            value["event_resource_data"]
        )
    out["attemptCount"] = value.get("attempt_count", 0)
    out["maxAttemptsCount"] = value.get("max_attempts_count", 0)
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
    if data.get("conversionProperties") is not None:
        import capo_drs.types.conversion_properties

        out["conversion_properties"] = (
            capo_drs.types.conversion_properties.deserialize_json(
                data["conversionProperties"]
            )
        )
    if data.get("eventResourceData") is not None:
        import capo_drs.types.event_resource_data

        out["event_resource_data"] = (
            capo_drs.types.event_resource_data.deserialize_json(
                data["eventResourceData"]
            )
        )
    if data.get("attemptCount") is not None:
        out["attempt_count"] = data["attemptCount"]
    else:
        out["attempt_count"] = 0
    if data.get("maxAttemptsCount") is not None:
        out["max_attempts_count"] = data["maxAttemptsCount"]
    else:
        out["max_attempts_count"] = 0
    return out
