"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#PolicyEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.policy_event

PolicyEventList: TypeAlias = list["capo_resiliencehubv2.types.policy_event.PolicyEvent"]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyEventList) -> list:
    import capo_resiliencehubv2.types.policy_event

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.policy_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> PolicyEventList:
    import capo_resiliencehubv2.types.policy_event

    out: PolicyEventList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_resiliencehubv2.types.policy_event.deserialize_json(item))
    return out
