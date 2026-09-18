"""Generated from Smithy shape ``com.amazonaws.omics#RunSummary``."""

from typing_extensions import NotRequired, TypedDict


class RunSummary(TypedDict, closed=True):
    pending_run_count: NotRequired["int"]
    """<p>The number of pending runs.</p>"""
    starting_run_count: NotRequired["int"]
    """<p>The number of starting runs.</p>"""
    running_run_count: NotRequired["int"]
    """<p>The number of running runs.</p>"""
    stopping_run_count: NotRequired["int"]
    """<p>The number of stopping runs.</p>"""
    completed_run_count: NotRequired["int"]
    """<p>The number of completed runs.</p>"""
    deleted_run_count: NotRequired["int"]
    """<p>The number of deleted runs.</p>"""
    failed_run_count: NotRequired["int"]
    """<p>The number of failed runs.</p>"""
    cancelled_run_count: NotRequired["int"]
    """<p>The number of cancelled runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RunSummary) -> dict:
    out: dict = {}
    if "pending_run_count" in value:
        out["pendingRunCount"] = value["pending_run_count"]
    if "starting_run_count" in value:
        out["startingRunCount"] = value["starting_run_count"]
    if "running_run_count" in value:
        out["runningRunCount"] = value["running_run_count"]
    if "stopping_run_count" in value:
        out["stoppingRunCount"] = value["stopping_run_count"]
    if "completed_run_count" in value:
        out["completedRunCount"] = value["completed_run_count"]
    if "deleted_run_count" in value:
        out["deletedRunCount"] = value["deleted_run_count"]
    if "failed_run_count" in value:
        out["failedRunCount"] = value["failed_run_count"]
    if "cancelled_run_count" in value:
        out["cancelledRunCount"] = value["cancelled_run_count"]
    return out


def deserialize_json(data: dict) -> RunSummary:
    out: RunSummary = {}  # type: ignore[typeddict-item]
    if data.get("pendingRunCount") is not None:
        out["pending_run_count"] = data["pendingRunCount"]
    if data.get("startingRunCount") is not None:
        out["starting_run_count"] = data["startingRunCount"]
    if data.get("runningRunCount") is not None:
        out["running_run_count"] = data["runningRunCount"]
    if data.get("stoppingRunCount") is not None:
        out["stopping_run_count"] = data["stoppingRunCount"]
    if data.get("completedRunCount") is not None:
        out["completed_run_count"] = data["completedRunCount"]
    if data.get("deletedRunCount") is not None:
        out["deleted_run_count"] = data["deletedRunCount"]
    if data.get("failedRunCount") is not None:
        out["failed_run_count"] = data["failedRunCount"]
    if data.get("cancelledRunCount") is not None:
        out["cancelled_run_count"] = data["cancelledRunCount"]
    return out
