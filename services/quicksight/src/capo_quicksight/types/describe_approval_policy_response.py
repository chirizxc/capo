"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeApprovalPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.approval_policy


class DescribeApprovalPolicyResponse(TypedDict, closed=True):
    policy: "capo_quicksight.types.approval_policy.ApprovalPolicy"
    """<p>The approval policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeApprovalPolicyResponse) -> dict:
    out: dict = {}
    import capo_quicksight.types.approval_policy

    out["Policy"] = capo_quicksight.types.approval_policy.serialize_json(
        value["policy"]
    )
    return out


def deserialize_json(data: dict) -> DescribeApprovalPolicyResponse:
    out: DescribeApprovalPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("Policy") is not None:
        import capo_quicksight.types.approval_policy

        out["policy"] = capo_quicksight.types.approval_policy.deserialize_json(
            data["Policy"]
        )
    else:
        raise DeserializationError("DescribeApprovalPolicyResponse.policy required")
    return out
