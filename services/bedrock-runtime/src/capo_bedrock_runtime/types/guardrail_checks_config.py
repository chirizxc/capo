"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_content_filter_config
    import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_config
    import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_config


class GuardrailChecksConfig(TypedDict, closed=True):
    content_filter: NotRequired[
        "capo_bedrock_runtime.types.guardrail_checks_content_filter_config.GuardrailChecksContentFilterConfig"
    ]
    """<p>The content filter check configuration.</p>"""
    prompt_attack: NotRequired[
        "capo_bedrock_runtime.types.guardrail_checks_prompt_attack_config.GuardrailChecksPromptAttackConfig"
    ]
    """<p>The prompt attack check configuration.</p>"""
    sensitive_information: NotRequired[
        "capo_bedrock_runtime.types.guardrail_checks_sensitive_information_config.GuardrailChecksSensitiveInformationConfig"
    ]
    """<p>The sensitive information check configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksConfig) -> dict:
    out: dict = {}
    if "content_filter" in value:
        import capo_bedrock_runtime.types.guardrail_checks_content_filter_config

        out["contentFilter"] = (
            capo_bedrock_runtime.types.guardrail_checks_content_filter_config.serialize_json(
                value["content_filter"]
            )
        )
    if "prompt_attack" in value:
        import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_config

        out["promptAttack"] = (
            capo_bedrock_runtime.types.guardrail_checks_prompt_attack_config.serialize_json(
                value["prompt_attack"]
            )
        )
    if "sensitive_information" in value:
        import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_config

        out["sensitiveInformation"] = (
            capo_bedrock_runtime.types.guardrail_checks_sensitive_information_config.serialize_json(
                value["sensitive_information"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailChecksConfig:
    out: GuardrailChecksConfig = {}  # type: ignore[typeddict-item]
    if data.get("contentFilter") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_content_filter_config

        out["content_filter"] = (
            capo_bedrock_runtime.types.guardrail_checks_content_filter_config.deserialize_json(
                data["contentFilter"]
            )
        )
    if data.get("promptAttack") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_config

        out["prompt_attack"] = (
            capo_bedrock_runtime.types.guardrail_checks_prompt_attack_config.deserialize_json(
                data["promptAttack"]
            )
        )
    if data.get("sensitiveInformation") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_config

        out["sensitive_information"] = (
            capo_bedrock_runtime.types.guardrail_checks_sensitive_information_config.deserialize_json(
                data["sensitiveInformation"]
            )
        )
    return out
