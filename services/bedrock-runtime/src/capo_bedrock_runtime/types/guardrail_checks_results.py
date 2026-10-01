"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksResults``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_content_filter_result
    import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_result
    import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_result


class GuardrailChecksResults(TypedDict, closed=True):
    content_filter: NotRequired[
        "capo_bedrock_runtime.types.guardrail_checks_content_filter_result.GuardrailChecksContentFilterResult"
    ]
    """<p>The content filter check results.</p>"""
    prompt_attack: NotRequired[
        "capo_bedrock_runtime.types.guardrail_checks_prompt_attack_result.GuardrailChecksPromptAttackResult"
    ]
    """<p>The prompt attack check results.</p>"""
    sensitive_information: NotRequired[
        "capo_bedrock_runtime.types.guardrail_checks_sensitive_information_result.GuardrailChecksSensitiveInformationResult"
    ]
    """<p>The sensitive information check results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksResults) -> dict:
    out: dict = {}
    if "content_filter" in value:
        import capo_bedrock_runtime.types.guardrail_checks_content_filter_result

        out["contentFilter"] = (
            capo_bedrock_runtime.types.guardrail_checks_content_filter_result.serialize_json(
                value["content_filter"]
            )
        )
    if "prompt_attack" in value:
        import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_result

        out["promptAttack"] = (
            capo_bedrock_runtime.types.guardrail_checks_prompt_attack_result.serialize_json(
                value["prompt_attack"]
            )
        )
    if "sensitive_information" in value:
        import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_result

        out["sensitiveInformation"] = (
            capo_bedrock_runtime.types.guardrail_checks_sensitive_information_result.serialize_json(
                value["sensitive_information"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailChecksResults:
    out: GuardrailChecksResults = {}  # type: ignore[typeddict-item]
    if data.get("contentFilter") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_content_filter_result

        out["content_filter"] = (
            capo_bedrock_runtime.types.guardrail_checks_content_filter_result.deserialize_json(
                data["contentFilter"]
            )
        )
    if data.get("promptAttack") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_result

        out["prompt_attack"] = (
            capo_bedrock_runtime.types.guardrail_checks_prompt_attack_result.deserialize_json(
                data["promptAttack"]
            )
        )
    if data.get("sensitiveInformation") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_result

        out["sensitive_information"] = (
            capo_bedrock_runtime.types.guardrail_checks_sensitive_information_result.deserialize_json(
                data["sensitiveInformation"]
            )
        )
    return out
