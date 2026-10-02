"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksUsageResults``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_content_filter_usage
    import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_usage
    import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_usage


class GuardrailChecksUsageResults(TypedDict, closed=True):
    content_filter: NotRequired[
        "capo_bedrock_runtime.types.guardrail_checks_content_filter_usage.GuardrailChecksContentFilterUsage"
    ]
    """<p>The text unit usage for the content filter check.</p>"""
    prompt_attack: NotRequired[
        "capo_bedrock_runtime.types.guardrail_checks_prompt_attack_usage.GuardrailChecksPromptAttackUsage"
    ]
    """<p>The text unit usage for the prompt attack check.</p>"""
    sensitive_information: NotRequired[
        "capo_bedrock_runtime.types.guardrail_checks_sensitive_information_usage.GuardrailChecksSensitiveInformationUsage"
    ]
    """<p>The text unit usage for the sensitive information check.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksUsageResults) -> dict:
    out: dict = {}
    if "content_filter" in value:
        import capo_bedrock_runtime.types.guardrail_checks_content_filter_usage

        out["contentFilter"] = (
            capo_bedrock_runtime.types.guardrail_checks_content_filter_usage.serialize_json(
                value["content_filter"]
            )
        )
    if "prompt_attack" in value:
        import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_usage

        out["promptAttack"] = (
            capo_bedrock_runtime.types.guardrail_checks_prompt_attack_usage.serialize_json(
                value["prompt_attack"]
            )
        )
    if "sensitive_information" in value:
        import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_usage

        out["sensitiveInformation"] = (
            capo_bedrock_runtime.types.guardrail_checks_sensitive_information_usage.serialize_json(
                value["sensitive_information"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailChecksUsageResults:
    out: GuardrailChecksUsageResults = {}  # type: ignore[typeddict-item]
    if data.get("contentFilter") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_content_filter_usage

        out["content_filter"] = (
            capo_bedrock_runtime.types.guardrail_checks_content_filter_usage.deserialize_json(
                data["contentFilter"]
            )
        )
    if data.get("promptAttack") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_usage

        out["prompt_attack"] = (
            capo_bedrock_runtime.types.guardrail_checks_prompt_attack_usage.deserialize_json(
                data["promptAttack"]
            )
        )
    if data.get("sensitiveInformation") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_usage

        out["sensitive_information"] = (
            capo_bedrock_runtime.types.guardrail_checks_sensitive_information_usage.deserialize_json(
                data["sensitiveInformation"]
            )
        )
    return out
