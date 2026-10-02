"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#PolicyDisassociationReason``."""

from typing import Literal, TypeAlias, cast

PolicyDisassociationReason: TypeAlias = Literal[
    "REPLACED_BY_UPDATE",
    "SHARING_REVOKED",
    "POLICY_DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyDisassociationReason) -> str:
    return value


def deserialize_json(data: str) -> PolicyDisassociationReason:
    return cast(PolicyDisassociationReason, data)
