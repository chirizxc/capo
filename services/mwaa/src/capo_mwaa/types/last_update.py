"""Generated from Smithy shape ``com.amazonaws.mwaa#LastUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa.types.update_created_at
    import capo_mwaa.types.update_error
    import capo_mwaa.types.update_source
    import capo_mwaa.types.update_status
    import capo_mwaa.types.worker_replacement_strategy


class LastUpdate(TypedDict, closed=True):
    status: NotRequired["capo_mwaa.types.update_status.UpdateStatus"]
    """<p>The status of the last update on the environment.</p>"""
    created_at: NotRequired["capo_mwaa.types.update_created_at.UpdateCreatedAt"]
    """<p>The day and time of the last update on the environment.</p>"""
    error: NotRequired["capo_mwaa.types.update_error.UpdateError"]
    """<p>The error that was encountered during the last update of the environment.</p>"""
    source: NotRequired["capo_mwaa.types.update_source.UpdateSource"]
    """<p>The source of the last update to the environment. Includes internal processes by Amazon MWAA, such as an environment maintenance update.</p>"""
    worker_replacement_strategy: NotRequired[
        "capo_mwaa.types.worker_replacement_strategy.WorkerReplacementStrategy"
    ]
    """<p>The worker replacement strategy used in the last update of the environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LastUpdate) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    if "created_at" in value:
        import capo_mwaa.types.update_created_at

        out["CreatedAt"] = capo_mwaa.types.update_created_at.serialize_json(
            value["created_at"]
        )
    if "error" in value:
        import capo_mwaa.types.update_error

        out["Error"] = capo_mwaa.types.update_error.serialize_json(value["error"])
    if "source" in value:
        out["Source"] = value["source"]
    if "worker_replacement_strategy" in value:
        out["WorkerReplacementStrategy"] = value["worker_replacement_strategy"]
    return out


def deserialize_json(data: dict) -> LastUpdate:
    out: LastUpdate = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("CreatedAt") is not None:
        import capo_mwaa.types.update_created_at

        out["created_at"] = capo_mwaa.types.update_created_at.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("Error") is not None:
        import capo_mwaa.types.update_error

        out["error"] = capo_mwaa.types.update_error.deserialize_json(data["Error"])
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    if data.get("WorkerReplacementStrategy") is not None:
        out["worker_replacement_strategy"] = data["WorkerReplacementStrategy"]
    return out
