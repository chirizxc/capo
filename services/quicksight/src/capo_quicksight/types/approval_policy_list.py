"""Generated from Smithy shape ``com.amazonaws.quicksight#ApprovalPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.approval_policy

ApprovalPolicyList: TypeAlias = list[
    "capo_quicksight.types.approval_policy.ApprovalPolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalPolicyList) -> list:
    import capo_quicksight.types.approval_policy

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.approval_policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApprovalPolicyList:
    import capo_quicksight.types.approval_policy

    out: ApprovalPolicyList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.approval_policy.deserialize_json(item))
    return out
