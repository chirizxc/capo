"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteApprovalPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.policy_id


class DeleteApprovalPolicyRequest(TypedDict, closed=True):
    policy_id: "capo_quicksight.types.policy_id.PolicyId"
    """<p>The unique identifier of the approval policy to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteApprovalPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteApprovalPolicyRequest:
    out: DeleteApprovalPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
