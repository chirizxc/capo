"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SigningAlgorithm``."""

from typing import Literal, TypeAlias, cast

SigningAlgorithm: TypeAlias = Literal[
    "RS256",
    "PS256",
    "ES256",
]


# --- restJson1 ser/de ---
def serialize_json(value: SigningAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> SigningAlgorithm:
    return cast(SigningAlgorithm, data)
