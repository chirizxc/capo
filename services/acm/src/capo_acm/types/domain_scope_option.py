"""Generated from Smithy shape ``com.amazonaws.acm#DomainScopeOption``."""

from typing import Literal, TypeAlias, cast

DomainScopeOption: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainScopeOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DomainScopeOption:
    return cast(DomainScopeOption, data)
