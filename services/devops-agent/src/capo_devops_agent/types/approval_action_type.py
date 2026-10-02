"""Generated from Smithy shape ``com.amazonaws.devopsagent#ApprovalActionType``."""

from typing import Literal, TypeAlias, cast

"""<p>The action to take on an approval request — APPROVED or REJECTED.</p>"""
ApprovalActionType: TypeAlias = Literal[
    "APPROVED",
    "REJECTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalActionType) -> str:
    return value


def deserialize_json(data: str) -> ApprovalActionType:
    return cast(ApprovalActionType, data)
