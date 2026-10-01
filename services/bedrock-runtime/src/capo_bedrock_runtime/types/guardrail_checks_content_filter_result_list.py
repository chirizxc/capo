"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksContentFilterResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_content_filter_result_entry

GuardrailChecksContentFilterResultList: TypeAlias = list[
    "capo_bedrock_runtime.types.guardrail_checks_content_filter_result_entry.GuardrailChecksContentFilterResultEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksContentFilterResultList) -> list:
    import capo_bedrock_runtime.types.guardrail_checks_content_filter_result_entry

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_runtime.types.guardrail_checks_content_filter_result_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailChecksContentFilterResultList:
    import capo_bedrock_runtime.types.guardrail_checks_content_filter_result_entry

    out: GuardrailChecksContentFilterResultList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_runtime.types.guardrail_checks_content_filter_result_entry.deserialize_json(
                item
            )
        )
    return out
