"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#JobExecutionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_jobs_data_plane.types.execution_number
    import capo_iot_jobs_data_plane.types.job_id
    import capo_iot_jobs_data_plane.types.last_updated_at
    import capo_iot_jobs_data_plane.types.queued_at
    import capo_iot_jobs_data_plane.types.started_at
    import capo_iot_jobs_data_plane.types.version_number


class JobExecutionSummary(TypedDict, closed=True):
    job_id: NotRequired["capo_iot_jobs_data_plane.types.job_id.JobId"]
    """<p>The unique identifier you assigned to this job when it was created.</p>"""
    queued_at: "capo_iot_jobs_data_plane.types.queued_at.QueuedAt"
    """<p>The time, in seconds since the epoch, when the job execution was enqueued.</p>"""
    started_at: NotRequired["capo_iot_jobs_data_plane.types.started_at.StartedAt"]
    """<p>The time, in seconds since the epoch, when the job execution started.</p>"""
    last_updated_at: "capo_iot_jobs_data_plane.types.last_updated_at.LastUpdatedAt"
    """<p>The time, in seconds since the epoch, when the job execution was last updated.</p>"""
    version_number: "capo_iot_jobs_data_plane.types.version_number.VersionNumber"
    """<p>The version of the job execution. Job execution versions are incremented each time IoT Jobs receives an update from a device.</p>"""
    execution_number: NotRequired[
        "capo_iot_jobs_data_plane.types.execution_number.ExecutionNumber"
    ]
    """<p>A number that identifies a particular job execution on a particular device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobExecutionSummary) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    out["queuedAt"] = value.get("queued_at", 0)
    if "started_at" in value:
        out["startedAt"] = value["started_at"]
    out["lastUpdatedAt"] = value.get("last_updated_at", 0)
    out["versionNumber"] = value.get("version_number", 0)
    if "execution_number" in value:
        out["executionNumber"] = value["execution_number"]
    return out


def deserialize_json(data: dict) -> JobExecutionSummary:
    out: JobExecutionSummary = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    if data.get("queuedAt") is not None:
        out["queued_at"] = data["queuedAt"]
    else:
        out["queued_at"] = 0
    if data.get("startedAt") is not None:
        out["started_at"] = data["startedAt"]
    if data.get("lastUpdatedAt") is not None:
        out["last_updated_at"] = data["lastUpdatedAt"]
    else:
        out["last_updated_at"] = 0
    if data.get("versionNumber") is not None:
        out["version_number"] = data["versionNumber"]
    else:
        out["version_number"] = 0
    if data.get("executionNumber") is not None:
        out["execution_number"] = data["executionNumber"]
    return out
