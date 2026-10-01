"""Generated from Smithy shape ``com.amazonaws.launchwizard#WorkloadDataSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_launch_wizard.types.account_constraints_list
    import capo_launch_wizard.types.workload_name
    import capo_launch_wizard.types.workload_status


class WorkloadDataSummary(TypedDict, closed=True):
    workload_name: NotRequired["capo_launch_wizard.types.workload_name.WorkloadName"]
    """<p>The name of the workload.</p>"""
    display_name: NotRequired["str"]
    """<p>The display name of the workload data.</p>"""
    status: NotRequired["capo_launch_wizard.types.workload_status.WorkloadStatus"]
    """<p>The status of the workload.</p>"""
    account_constraints: NotRequired[
        "capo_launch_wizard.types.account_constraints_list.AccountConstraintsList"
    ]
    """Optional list of constraints describing what kind of AWS account is allowed to deploy this workload or deployment pattern. Within a single list the semantics are OR: an account satisfies the list if it satisfies any entry. Workload-level and pattern-level lists combine with AND at deployment time. An absent or empty list at this level means no constraint at this level."""


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadDataSummary) -> dict:
    out: dict = {}
    if "workload_name" in value:
        out["workloadName"] = value["workload_name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "status" in value:
        import capo_launch_wizard.types.workload_status

        out["status"] = capo_launch_wizard.types.workload_status.serialize_json(
            value["status"]
        )
    if "account_constraints" in value:
        import capo_launch_wizard.types.account_constraints_list

        out["accountConstraints"] = (
            capo_launch_wizard.types.account_constraints_list.serialize_json(
                value["account_constraints"]
            )
        )
    return out


def deserialize_json(data: dict) -> WorkloadDataSummary:
    out: WorkloadDataSummary = {}  # type: ignore[typeddict-item]
    if data.get("workloadName") is not None:
        out["workload_name"] = data["workloadName"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("status") is not None:
        import capo_launch_wizard.types.workload_status

        out["status"] = capo_launch_wizard.types.workload_status.deserialize_json(
            data["status"]
        )
    if data.get("accountConstraints") is not None:
        import capo_launch_wizard.types.account_constraints_list

        out["account_constraints"] = (
            capo_launch_wizard.types.account_constraints_list.deserialize_json(
                data["accountConstraints"]
            )
        )
    return out
