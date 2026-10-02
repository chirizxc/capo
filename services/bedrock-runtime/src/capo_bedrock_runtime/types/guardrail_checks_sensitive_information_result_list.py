"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksSensitiveInformationResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_result_entry

GuardrailChecksSensitiveInformationResultList: TypeAlias = list[
    "capo_bedrock_runtime.types.guardrail_checks_sensitive_information_result_entry.GuardrailChecksSensitiveInformationResultEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksSensitiveInformationResultList) -> list:
    import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_result_entry

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_runtime.types.guardrail_checks_sensitive_information_result_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailChecksSensitiveInformationResultList:
    import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_result_entry

    out: GuardrailChecksSensitiveInformationResultList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_runtime.types.guardrail_checks_sensitive_information_result_entry.deserialize_json(
                item
            )
        )
    return out
