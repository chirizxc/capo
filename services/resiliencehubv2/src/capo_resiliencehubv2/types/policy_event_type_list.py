"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#PolicyEventTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.policy_event_type

PolicyEventTypeList: TypeAlias = list[
    "capo_resiliencehubv2.types.policy_event_type.PolicyEventType"
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyEventTypeList) -> list:
    import capo_resiliencehubv2.types.policy_event_type

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.policy_event_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> PolicyEventTypeList:
    import capo_resiliencehubv2.types.policy_event_type

    out: PolicyEventTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_resiliencehubv2.types.policy_event_type.deserialize_json(item))
    return out
