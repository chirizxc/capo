"""Generated from Smithy shape ``com.amazonaws.batch#CancelJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.string
    import capo_batch.types.string_list


class CancelJobsRequest(TypedDict, closed=True):
    jobs: NotRequired["capo_batch.types.string_list.StringList"]
    """<p>An array of up to 50 Batch job IDs of the jobs to cancel.</p>"""
    reason: NotRequired["capo_batch.types.string.String"]
    """<p>A message to attach to the job that explains the reason for cancelling it. This message is returned by future <a>DescribeJobs</a> operations on the job. It is also recorded in the Batch activity logs.</p> <p>This parameter has a limit of 1024 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobsRequest) -> dict:
    out: dict = {}
    if "jobs" in value:
        import capo_batch.types.string_list

        out["jobs"] = capo_batch.types.string_list.serialize_json(value["jobs"])
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> CancelJobsRequest:
    out: CancelJobsRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobs") is not None:
        import capo_batch.types.string_list

        out["jobs"] = capo_batch.types.string_list.deserialize_json(data["jobs"])
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out
