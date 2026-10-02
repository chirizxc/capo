"""Generated from Smithy shape ``com.amazonaws.batch#TerminateServiceJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.string
    import capo_batch.types.string_list


class TerminateServiceJobsRequest(TypedDict, closed=True):
    jobs: NotRequired["capo_batch.types.string_list.StringList"]
    """<p>An array of up to 50 service job IDs of the service jobs to terminate.</p>"""
    reason: NotRequired["capo_batch.types.string.String"]
    """<p>A message to attach to the service job that explains the reason for terminating it. This message is returned by <code>DescribeServiceJob</code> operations on the service job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TerminateServiceJobsRequest) -> dict:
    out: dict = {}
    if "jobs" in value:
        import capo_batch.types.string_list

        out["jobs"] = capo_batch.types.string_list.serialize_json(value["jobs"])
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> TerminateServiceJobsRequest:
    out: TerminateServiceJobsRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobs") is not None:
        import capo_batch.types.string_list

        out["jobs"] = capo_batch.types.string_list.deserialize_json(data["jobs"])
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out
