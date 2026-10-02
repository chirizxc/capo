"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CoinbaseCdpSecrets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.coinbase_cdp_secret

CoinbaseCdpSecrets: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.coinbase_cdp_secret.CoinbaseCdpSecret"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoinbaseCdpSecrets) -> list:
    import capo_bedrock_agentcore_control.types.coinbase_cdp_secret

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.coinbase_cdp_secret.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CoinbaseCdpSecrets:
    import capo_bedrock_agentcore_control.types.coinbase_cdp_secret

    out: CoinbaseCdpSecrets = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.coinbase_cdp_secret.deserialize_json(
                item
            )
        )
    return out
