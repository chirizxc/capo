"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksPromptAttackResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_result_entry

GuardrailChecksPromptAttackResultList: TypeAlias = list[
    "capo_bedrock_runtime.types.guardrail_checks_prompt_attack_result_entry.GuardrailChecksPromptAttackResultEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksPromptAttackResultList) -> list:
    import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_result_entry

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_runtime.types.guardrail_checks_prompt_attack_result_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailChecksPromptAttackResultList:
    import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_result_entry

    out: GuardrailChecksPromptAttackResultList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_runtime.types.guardrail_checks_prompt_attack_result_entry.deserialize_json(
                item
            )
        )
    return out
