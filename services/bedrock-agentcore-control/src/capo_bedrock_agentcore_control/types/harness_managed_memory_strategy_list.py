"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessManagedMemoryStrategyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_managed_memory_strategy_type

HarnessManagedMemoryStrategyList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.harness_managed_memory_strategy_type.HarnessManagedMemoryStrategyType"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessManagedMemoryStrategyList) -> list:
    import capo_bedrock_agentcore_control.types.harness_managed_memory_strategy_type

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.harness_managed_memory_strategy_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> HarnessManagedMemoryStrategyList:
    import capo_bedrock_agentcore_control.types.harness_managed_memory_strategy_type

    out: HarnessManagedMemoryStrategyList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.harness_managed_memory_strategy_type.deserialize_json(
                item
            )
        )
    return out
