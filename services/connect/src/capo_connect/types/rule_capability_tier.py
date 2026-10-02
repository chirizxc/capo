"""Generated from Smithy shape ``com.amazonaws.connect#RuleCapabilityTier``."""

from typing import Literal, TypeAlias, cast

RuleCapabilityTier: TypeAlias = Literal["GenerativeAI",]


# --- restJson1 ser/de ---
def serialize_json(value: RuleCapabilityTier) -> str:
    return value


def deserialize_json(data: str) -> RuleCapabilityTier:
    return cast(RuleCapabilityTier, data)
