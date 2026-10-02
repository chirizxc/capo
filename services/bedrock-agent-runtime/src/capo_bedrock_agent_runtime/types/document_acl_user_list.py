"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#DocumentAclUserList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.document_acl_user

DocumentAclUserList: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.document_acl_user.DocumentAclUser"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAclUserList) -> list:
    import capo_bedrock_agent_runtime.types.document_acl_user

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.document_acl_user.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DocumentAclUserList:
    import capo_bedrock_agent_runtime.types.document_acl_user

    out: DocumentAclUserList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.document_acl_user.deserialize_json(item)
        )
    return out
