"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#DocumentAclConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.document_acl_condition

DocumentAclConditionList: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.document_acl_condition.DocumentAclCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAclConditionList) -> list:
    import capo_bedrock_agent_runtime.types.document_acl_condition

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.document_acl_condition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DocumentAclConditionList:
    import capo_bedrock_agent_runtime.types.document_acl_condition

    out: DocumentAclConditionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.document_acl_condition.deserialize_json(
                item
            )
        )
    return out
