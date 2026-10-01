"""Generated from Smithy shape ``com.amazonaws.guardduty#ContentPolicyFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.content_policy_filter

ContentPolicyFilters: TypeAlias = list[
    "capo_guardduty.types.content_policy_filter.ContentPolicyFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentPolicyFilters) -> list:
    import capo_guardduty.types.content_policy_filter

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.content_policy_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContentPolicyFilters:
    import capo_guardduty.types.content_policy_filter

    out: ContentPolicyFilters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.content_policy_filter.deserialize_json(item))
    return out
