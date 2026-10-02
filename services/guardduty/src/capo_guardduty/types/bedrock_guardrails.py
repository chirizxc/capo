"""Generated from Smithy shape ``com.amazonaws.guardduty#BedrockGuardrails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.bedrock_guardrail

BedrockGuardrails: TypeAlias = list[
    "capo_guardduty.types.bedrock_guardrail.BedrockGuardrail"
]


# --- restJson1 ser/de ---
def serialize_json(value: BedrockGuardrails) -> list:
    import capo_guardduty.types.bedrock_guardrail

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.bedrock_guardrail.serialize_json(item))
    return out


def deserialize_json(data: list) -> BedrockGuardrails:
    import capo_guardduty.types.bedrock_guardrail

    out: BedrockGuardrails = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.bedrock_guardrail.deserialize_json(item))
    return out
