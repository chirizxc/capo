"""Generated from Smithy shape ``com.amazonaws.batch#TerminateJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.string_list
    import capo_batch.types.terminate_jobs_error_detail_list


class TerminateJobsResponse(TypedDict, closed=True):
    successful: NotRequired["capo_batch.types.string_list.StringList"]
    """<p>A list of the job IDs whose termination request was accepted.</p>"""
    errors: NotRequired[
        "capo_batch.types.terminate_jobs_error_detail_list.TerminateJobsErrorDetailList"
    ]
    """<p>A list of <code>TerminateJobsErrorDetail</code> items, one for each job that couldn't be terminated. Each item includes the job ID along with a code and message that describe why the job wasn't terminated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TerminateJobsResponse) -> dict:
    out: dict = {}
    if "successful" in value:
        import capo_batch.types.string_list

        out["successful"] = capo_batch.types.string_list.serialize_json(
            value["successful"]
        )
    if "errors" in value:
        import capo_batch.types.terminate_jobs_error_detail_list

        out["errors"] = (
            capo_batch.types.terminate_jobs_error_detail_list.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> TerminateJobsResponse:
    out: TerminateJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("successful") is not None:
        import capo_batch.types.string_list

        out["successful"] = capo_batch.types.string_list.deserialize_json(
            data["successful"]
        )
    if data.get("errors") is not None:
        import capo_batch.types.terminate_jobs_error_detail_list

        out["errors"] = (
            capo_batch.types.terminate_jobs_error_detail_list.deserialize_json(
                data["errors"]
            )
        )
    return out
