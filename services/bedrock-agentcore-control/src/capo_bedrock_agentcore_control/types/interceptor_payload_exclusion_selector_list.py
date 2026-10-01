"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InterceptorPayloadExclusionSelectorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.interceptor_payload_exclusion_selector

InterceptorPayloadExclusionSelectorList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.interceptor_payload_exclusion_selector.InterceptorPayloadExclusionSelector"
]


# --- restJson1 ser/de ---
def serialize_json(value: InterceptorPayloadExclusionSelectorList) -> list:
    import capo_bedrock_agentcore_control.types.interceptor_payload_exclusion_selector

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.interceptor_payload_exclusion_selector.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InterceptorPayloadExclusionSelectorList:
    import capo_bedrock_agentcore_control.types.interceptor_payload_exclusion_selector

    out: InterceptorPayloadExclusionSelectorList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.interceptor_payload_exclusion_selector.deserialize_json(
                item
            )
        )
    return out
