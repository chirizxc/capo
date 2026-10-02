"""Generated from Smithy shape ``com.amazonaws.guardduty#RuleSchema``."""

from typing import Literal, TypeAlias, cast

RuleSchema: TypeAlias = Literal["CloudTrail",]


# --- restJson1 ser/de ---
def serialize_json(value: RuleSchema) -> str:
    return value


def deserialize_json(data: str) -> RuleSchema:
    return cast(RuleSchema, data)
