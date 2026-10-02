"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AccountTargeting``."""

from typing import Literal, TypeAlias, cast

"""Whether a test run targets resources in a single AWS account or across multiple accounts."""
AccountTargeting: TypeAlias = Literal[
    "SINGLE_ACCOUNT",
    "MULTI_ACCOUNT",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountTargeting) -> str:
    return value


def deserialize_json(data: str) -> AccountTargeting:
    return cast(AccountTargeting, data)
