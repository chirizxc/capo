"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksPromptAttackCategoryConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category_config

GuardrailChecksPromptAttackCategoryConfigList: TypeAlias = list[
    "capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category_config.GuardrailChecksPromptAttackCategoryConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksPromptAttackCategoryConfigList) -> list:
    import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category_config

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category_config.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailChecksPromptAttackCategoryConfigList:
    import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category_config

    out: GuardrailChecksPromptAttackCategoryConfigList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category_config.deserialize_json(
                item
            )
        )
    return out
