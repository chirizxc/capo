"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeApprovalPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.policy_id


class DescribeApprovalPolicyRequest(TypedDict, closed=True):
    policy_id: "capo_quicksight.types.policy_id.PolicyId"
    """<p>The unique identifier of the approval policy to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeApprovalPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeApprovalPolicyRequest:
    out: DescribeApprovalPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
