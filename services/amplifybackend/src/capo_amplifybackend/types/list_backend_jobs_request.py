"""Generated from Smithy shape ``com.amazonaws.amplifybackend#ListBackendJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__integer_min1_max25
    import capo_amplifybackend.types.__string


class ListBackendJobsRequest(TypedDict, closed=True):
    app_id: "capo_amplifybackend.types.__string.__string"
    """<p>The app ID.</p>"""
    backend_environment_name: "capo_amplifybackend.types.__string.__string"
    """<p>The name of the backend environment.</p>"""
    job_id: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The ID for the job.</p>"""
    max_results: NotRequired[
        "capo_amplifybackend.types.__integer_min1_max25.__integerMin1Max25"
    ]
    """<p>The maximum number of results that you want in the response.</p>"""
    next_token: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The token for the next set of results.</p>"""
    operation: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>Filters the list of response objects to include only those with the specified operation name.</p>"""
    status: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>Filters the list of response objects to include only those with the specified status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBackendJobsRequest) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "operation" in value:
        out["operation"] = value["operation"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> ListBackendJobsRequest:
    out: ListBackendJobsRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("operation") is not None:
        out["operation"] = data["operation"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    return out
