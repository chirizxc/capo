"""Generated from Smithy shape ``com.amazonaws.batch#CancelJobsErrorDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.string


class CancelJobsErrorDetail(TypedDict, closed=True):
    job: NotRequired["capo_batch.types.string.String"]
    """<p>The Batch job ID of the job that couldn't be cancelled.</p>"""
    code: NotRequired["capo_batch.types.string.String"]
    """<p>An error code that identifies the reason the job couldn't be cancelled. Valid values are:</p> <ul> <li> <p> <code>ValidationException</code> – A job identifier in the request is malformed or isn't valid.</p> </li> <li> <p> <code>ClientException</code> – The request failed because of a client error.</p> </li> <li> <p> <code>ThrottlingException</code> – The request was throttled. Retry the request.</p> </li> <li> <p> <code>ServerException</code> – An internal error occurred. Retry the request.</p> </li> <li> <p> <code>AccessDenied</code> – The caller isn't authorized to perform the action on the specified job.</p> </li> </ul>"""
    message: NotRequired["capo_batch.types.string.String"]
    """<p>A message that describes the reason the job couldn't be cancelled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobsErrorDetail) -> dict:
    out: dict = {}
    if "job" in value:
        out["job"] = value["job"]
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CancelJobsErrorDetail:
    out: CancelJobsErrorDetail = {}  # type: ignore[typeddict-item]
    if data.get("job") is not None:
        out["job"] = data["job"]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
