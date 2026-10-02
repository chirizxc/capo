"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RateConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.rate_config

RateConfigs: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.rate_config.RateConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: RateConfigs) -> list:
    import capo_bedrock_agentcore_control.types.rate_config

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.rate_config.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RateConfigs:
    import capo_bedrock_agentcore_control.types.rate_config

    out: RateConfigs = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.rate_config.deserialize_json(item)
        )
    return out
