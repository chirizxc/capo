"""Generated from Smithy shape ``com.amazonaws.connect#RuleCapabilityTiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.rule_capability_tier

RuleCapabilityTiers: TypeAlias = list[
    "capo_connect.types.rule_capability_tier.RuleCapabilityTier"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleCapabilityTiers) -> list:
    import capo_connect.types.rule_capability_tier

    out: list = []
    for item in value:
        out.append(capo_connect.types.rule_capability_tier.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuleCapabilityTiers:
    import capo_connect.types.rule_capability_tier

    out: RuleCapabilityTiers = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.rule_capability_tier.deserialize_json(item))
    return out
