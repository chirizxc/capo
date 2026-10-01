"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#PolicyEventType``."""

from typing import Literal, TypeAlias, cast

PolicyEventType: TypeAlias = Literal[
    "POLICY_ATTACHED_TO_SERVICE",
    "POLICY_DETACHED_FROM_SERVICE",
    "POLICY_SHARING_REVOKED",
    "POLICY_DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyEventType) -> str:
    return value


def deserialize_json(data: str) -> PolicyEventType:
    return cast(PolicyEventType, data)
