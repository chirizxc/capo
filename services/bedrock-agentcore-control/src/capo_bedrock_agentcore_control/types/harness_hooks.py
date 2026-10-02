"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessHooks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_hook

HarnessHooks: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.harness_hook.HarnessHook"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessHooks) -> list:
    import capo_bedrock_agentcore_control.types.harness_hook

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.harness_hook.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> HarnessHooks:
    import capo_bedrock_agentcore_control.types.harness_hook

    out: HarnessHooks = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.harness_hook.deserialize_json(item)
        )
    return out
