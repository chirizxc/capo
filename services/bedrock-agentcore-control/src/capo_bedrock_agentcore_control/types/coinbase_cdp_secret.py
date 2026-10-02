"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CoinbaseCdpSecret``."""

from typing import Literal, TypeAlias, cast

CoinbaseCdpSecret: TypeAlias = Literal[
    "API_KEY",
    "WALLET_SECRET",
]


# --- restJson1 ser/de ---
def serialize_json(value: CoinbaseCdpSecret) -> str:
    return value


def deserialize_json(data: str) -> CoinbaseCdpSecret:
    return cast(CoinbaseCdpSecret, data)
