"""Generated from Smithy shape ``com.amazonaws.batch#CancelJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.cancel_jobs_error_detail_list
    import capo_batch.types.string_list


class CancelJobsResponse(TypedDict, closed=True):
    successful: NotRequired["capo_batch.types.string_list.StringList"]
    """<p>A list of the job IDs whose cancellation request was accepted.</p>"""
    errors: NotRequired[
        "capo_batch.types.cancel_jobs_error_detail_list.CancelJobsErrorDetailList"
    ]
    """<p>A list of <code>CancelJobsErrorDetail</code> items, one for each job that couldn't be cancelled. Each item includes the job ID along with a code and message that describe why the job wasn't cancelled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobsResponse) -> dict:
    out: dict = {}
    if "successful" in value:
        import capo_batch.types.string_list

        out["successful"] = capo_batch.types.string_list.serialize_json(
            value["successful"]
        )
    if "errors" in value:
        import capo_batch.types.cancel_jobs_error_detail_list

        out["errors"] = capo_batch.types.cancel_jobs_error_detail_list.serialize_json(
            value["errors"]
        )
    return out


def deserialize_json(data: dict) -> CancelJobsResponse:
    out: CancelJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("successful") is not None:
        import capo_batch.types.string_list

        out["successful"] = capo_batch.types.string_list.deserialize_json(
            data["successful"]
        )
    if data.get("errors") is not None:
        import capo_batch.types.cancel_jobs_error_detail_list

        out["errors"] = capo_batch.types.cancel_jobs_error_detail_list.deserialize_json(
            data["errors"]
        )
    return out
