"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksContentFilterCategoryConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_content_filter_category_config

GuardrailChecksContentFilterCategoryConfigList: TypeAlias = list[
    "capo_bedrock_runtime.types.guardrail_checks_content_filter_category_config.GuardrailChecksContentFilterCategoryConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksContentFilterCategoryConfigList) -> list:
    import capo_bedrock_runtime.types.guardrail_checks_content_filter_category_config

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_runtime.types.guardrail_checks_content_filter_category_config.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailChecksContentFilterCategoryConfigList:
    import capo_bedrock_runtime.types.guardrail_checks_content_filter_category_config

    out: GuardrailChecksContentFilterCategoryConfigList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_runtime.types.guardrail_checks_content_filter_category_config.deserialize_json(
                item
            )
        )
    return out
