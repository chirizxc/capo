"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#DocumentAclCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.document_acl_group_list
    import capo_bedrock_agent_runtime.types.document_acl_member_relation
    import capo_bedrock_agent_runtime.types.document_acl_user_list


class DocumentAclCondition(TypedDict, closed=True):
    condition_operator: NotRequired[
        "capo_bedrock_agent_runtime.types.document_acl_member_relation.DocumentAclMemberRelation"
    ]
    """<p>The logical operator for combining users and groups within this condition. Valid values: <code>AND</code> – Both a user match and a group match are required. <code>OR</code> – Either a user match or a group match is sufficient.</p>"""
    users: NotRequired[
        "capo_bedrock_agent_runtime.types.document_acl_user_list.DocumentAclUserList"
    ]
    """<p>The list of user entries in this condition.</p>"""
    groups: NotRequired[
        "capo_bedrock_agent_runtime.types.document_acl_group_list.DocumentAclGroupList"
    ]
    """<p>The list of group entries in this condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAclCondition) -> dict:
    out: dict = {}
    if "condition_operator" in value:
        import capo_bedrock_agent_runtime.types.document_acl_member_relation

        out["conditionOperator"] = (
            capo_bedrock_agent_runtime.types.document_acl_member_relation.serialize_json(
                value["condition_operator"]
            )
        )
    if "users" in value:
        import capo_bedrock_agent_runtime.types.document_acl_user_list

        out["users"] = (
            capo_bedrock_agent_runtime.types.document_acl_user_list.serialize_json(
                value["users"]
            )
        )
    if "groups" in value:
        import capo_bedrock_agent_runtime.types.document_acl_group_list

        out["groups"] = (
            capo_bedrock_agent_runtime.types.document_acl_group_list.serialize_json(
                value["groups"]
            )
        )
    return out


def deserialize_json(data: dict) -> DocumentAclCondition:
    out: DocumentAclCondition = {}  # type: ignore[typeddict-item]
    if data.get("conditionOperator") is not None:
        import capo_bedrock_agent_runtime.types.document_acl_member_relation

        out["condition_operator"] = (
            capo_bedrock_agent_runtime.types.document_acl_member_relation.deserialize_json(
                data["conditionOperator"]
            )
        )
    if data.get("users") is not None:
        import capo_bedrock_agent_runtime.types.document_acl_user_list

        out["users"] = (
            capo_bedrock_agent_runtime.types.document_acl_user_list.deserialize_json(
                data["users"]
            )
        )
    if data.get("groups") is not None:
        import capo_bedrock_agent_runtime.types.document_acl_group_list

        out["groups"] = (
            capo_bedrock_agent_runtime.types.document_acl_group_list.deserialize_json(
                data["groups"]
            )
        )
    return out
