"""Generated from Smithy shape ``com.amazonaws.iot#TaskStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.canceled_checks_count
    import capo_iot.types.compliant_checks_count
    import capo_iot.types.failed_checks_count
    import capo_iot.types.in_progress_checks_count
    import capo_iot.types.non_compliant_checks_count
    import capo_iot.types.total_checks_count
    import capo_iot.types.waiting_for_data_collection_checks_count


class TaskStatistics(TypedDict, closed=True):
    total_checks: NotRequired["capo_iot.types.total_checks_count.TotalChecksCount"]
    """<p>The number of checks in this audit.</p>"""
    in_progress_checks: NotRequired[
        "capo_iot.types.in_progress_checks_count.InProgressChecksCount"
    ]
    """<p>The number of checks in progress.</p>"""
    waiting_for_data_collection_checks: NotRequired[
        "capo_iot.types.waiting_for_data_collection_checks_count.WaitingForDataCollectionChecksCount"
    ]
    """<p>The number of checks waiting for data collection.</p>"""
    compliant_checks: NotRequired[
        "capo_iot.types.compliant_checks_count.CompliantChecksCount"
    ]
    """<p>The number of checks that found compliant resources.</p>"""
    non_compliant_checks: NotRequired[
        "capo_iot.types.non_compliant_checks_count.NonCompliantChecksCount"
    ]
    """<p>The number of checks that found noncompliant resources.</p>"""
    failed_checks: NotRequired["capo_iot.types.failed_checks_count.FailedChecksCount"]
    """<p>The number of checks.</p>"""
    canceled_checks: NotRequired[
        "capo_iot.types.canceled_checks_count.CanceledChecksCount"
    ]
    """<p>The number of checks that did not run because the audit was canceled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskStatistics) -> dict:
    out: dict = {}
    if "total_checks" in value:
        out["totalChecks"] = value["total_checks"]
    if "in_progress_checks" in value:
        out["inProgressChecks"] = value["in_progress_checks"]
    if "waiting_for_data_collection_checks" in value:
        out["waitingForDataCollectionChecks"] = value[
            "waiting_for_data_collection_checks"
        ]
    if "compliant_checks" in value:
        out["compliantChecks"] = value["compliant_checks"]
    if "non_compliant_checks" in value:
        out["nonCompliantChecks"] = value["non_compliant_checks"]
    if "failed_checks" in value:
        out["failedChecks"] = value["failed_checks"]
    if "canceled_checks" in value:
        out["canceledChecks"] = value["canceled_checks"]
    return out


def deserialize_json(data: dict) -> TaskStatistics:
    out: TaskStatistics = {}  # type: ignore[typeddict-item]
    if data.get("totalChecks") is not None:
        out["total_checks"] = data["totalChecks"]
    if data.get("inProgressChecks") is not None:
        out["in_progress_checks"] = data["inProgressChecks"]
    if data.get("waitingForDataCollectionChecks") is not None:
        out["waiting_for_data_collection_checks"] = data[
            "waitingForDataCollectionChecks"
        ]
    if data.get("compliantChecks") is not None:
        out["compliant_checks"] = data["compliantChecks"]
    if data.get("nonCompliantChecks") is not None:
        out["non_compliant_checks"] = data["nonCompliantChecks"]
    if data.get("failedChecks") is not None:
        out["failed_checks"] = data["failedChecks"]
    if data.get("canceledChecks") is not None:
        out["canceled_checks"] = data["canceledChecks"]
    return out
