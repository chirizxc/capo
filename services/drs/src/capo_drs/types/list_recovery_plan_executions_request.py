"""Generated from Smithy shape ``com.amazonaws.drs#ListRecoveryPlanExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.max_results_type
    import capo_drs.types.pagination_token
    import capo_drs.types.recovery_plan_execution_status
    import capo_drs.types.strict_drsarn


class ListRecoveryPlanExecutionsRequest(TypedDict, closed=True):
    recovery_plan_arn: NotRequired["capo_drs.types.strict_drsarn.StrictDRSARN"]
    """<p>Filter executions by Recovery Plan ARN.</p>"""
    status: NotRequired[
        "capo_drs.types.recovery_plan_execution_status.RecoveryPlanExecutionStatus"
    ]
    """<p>Filter executions by status.</p>"""
    max_results: NotRequired["capo_drs.types.max_results_type.MaxResultsType"]
    """<p>Maximum number of results to return.</p>"""
    next_token: NotRequired["capo_drs.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecoveryPlanExecutionsRequest) -> dict:
    out: dict = {}
    if "recovery_plan_arn" in value:
        out["recoveryPlanArn"] = value["recovery_plan_arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecoveryPlanExecutionsRequest:
    out: ListRecoveryPlanExecutionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanArn") is not None:
        out["recovery_plan_arn"] = data["recoveryPlanArn"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
