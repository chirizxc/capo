"""Generated from Smithy shape ``com.amazonaws.bedrockagent#VpcConfigurationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.vpc_configuration_summary

VpcConfigurationSummaryList: TypeAlias = list[
    "capo_bedrock_agent.types.vpc_configuration_summary.VpcConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfigurationSummaryList) -> list:
    import capo_bedrock_agent.types.vpc_configuration_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent.types.vpc_configuration_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> VpcConfigurationSummaryList:
    import capo_bedrock_agent.types.vpc_configuration_summary

    out: VpcConfigurationSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent.types.vpc_configuration_summary.deserialize_json(item)
        )
    return out
