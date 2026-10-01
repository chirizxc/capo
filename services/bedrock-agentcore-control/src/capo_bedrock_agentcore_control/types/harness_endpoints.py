"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessEndpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_endpoint

HarnessEndpoints: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.harness_endpoint.HarnessEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessEndpoints) -> list:
    import capo_bedrock_agentcore_control.types.harness_endpoint

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.harness_endpoint.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> HarnessEndpoints:
    import capo_bedrock_agentcore_control.types.harness_endpoint

    out: HarnessEndpoints = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.harness_endpoint.deserialize_json(item)
        )
    return out
