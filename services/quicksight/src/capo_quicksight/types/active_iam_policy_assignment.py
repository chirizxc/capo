"""Generated from Smithy shape ``com.amazonaws.quicksight#ActiveIAMPolicyAssignment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.iam_policy_assignment_name


class ActiveIAMPolicyAssignment(TypedDict, closed=True):
    assignment_name: NotRequired[
        "capo_quicksight.types.iam_policy_assignment_name.IAMPolicyAssignmentName"
    ]
    """<p>A name for the IAM policy assignment.</p>"""
    policy_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActiveIAMPolicyAssignment) -> dict:
    out: dict = {}
    if "assignment_name" in value:
        out["AssignmentName"] = value["assignment_name"]
    if "policy_arn" in value:
        out["PolicyArn"] = value["policy_arn"]
    return out


def deserialize_json(data: dict) -> ActiveIAMPolicyAssignment:
    out: ActiveIAMPolicyAssignment = {}  # type: ignore[typeddict-item]
    if data.get("AssignmentName") is not None:
        out["assignment_name"] = data["AssignmentName"]
    if data.get("PolicyArn") is not None:
        out["policy_arn"] = data["PolicyArn"]
    return out
