"""Generated from Smithy shape ``com.amazonaws.guardduty#RuleLanguage``."""

from typing import Literal, TypeAlias, cast

RuleLanguage: TypeAlias = Literal["SQL",]


# --- restJson1 ser/de ---
def serialize_json(value: RuleLanguage) -> str:
    return value


def deserialize_json(data: str) -> RuleLanguage:
    return cast(RuleLanguage, data)
