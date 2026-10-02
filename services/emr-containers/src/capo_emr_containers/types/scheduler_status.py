"""Generated from Smithy shape ``com.amazonaws.emrcontainers#SchedulerStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.non_negative_integer


class SchedulerStatus(TypedDict, closed=True):
    current_in_queue_job_runs: (
        "capo_emr_containers.types.non_negative_integer.NonNegativeInteger"
    )
    """<p>The number of job runs currently waiting in the queue (<code>PENDING</code> or <code>SUBMITTED</code>) for the virtual cluster.</p>"""
    current_concurrent_job_runs: (
        "capo_emr_containers.types.non_negative_integer.NonNegativeInteger"
    )
    """<p>The number of job runs currently in the <code>RUNNING</code> state for the virtual cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchedulerStatus) -> dict:
    out: dict = {}
    out["currentInQueueJobRuns"] = value.get("current_in_queue_job_runs", 0)
    out["currentConcurrentJobRuns"] = value.get("current_concurrent_job_runs", 0)
    return out


def deserialize_json(data: dict) -> SchedulerStatus:
    out: SchedulerStatus = {}  # type: ignore[typeddict-item]
    if data.get("currentInQueueJobRuns") is not None:
        out["current_in_queue_job_runs"] = data["currentInQueueJobRuns"]
    else:
        out["current_in_queue_job_runs"] = 0
    if data.get("currentConcurrentJobRuns") is not None:
        out["current_concurrent_job_runs"] = data["currentConcurrentJobRuns"]
    else:
        out["current_concurrent_job_runs"] = 0
    return out
