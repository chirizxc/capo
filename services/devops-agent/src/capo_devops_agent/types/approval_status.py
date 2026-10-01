"""Generated from Smithy shape ``com.amazonaws.devopsagent#ApprovalStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Lifecycle status of an approval request, distinct from the action verb. State machine: PENDING (awaiting a decision) -&gt; APPROVED (the action was APPROVED; redeemable until revoked or fully redeemed) or REJECTED (the action was REJECTED; terminal). APPROVED -&gt; REDEEMED (consumed by a credential mint at least once; non-single-use approvals stay re-redeemable until expiry) or REVOKED (administratively invalidated; terminal).</p>"""
ApprovalStatus: TypeAlias = Literal[
    "PENDING",
    "APPROVED",
    "REJECTED",
    "REVOKED",
    "REDEEMED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalStatus) -> str:
    return value


def deserialize_json(data: str) -> ApprovalStatus:
    return cast(ApprovalStatus, data)
