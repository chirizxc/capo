"""Generated from Smithy shape ``com.amazonaws.wafv2#BlockchainChain``."""

from typing import Literal, TypeAlias, cast

BlockchainChain: TypeAlias = Literal[
    "BASE",
    "SOLANA",
    "BASE_SEPOLIA",
    "SOLANA_DEVNET",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlockchainChain) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BlockchainChain:
    return cast(BlockchainChain, data)
