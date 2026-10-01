"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#DocumentAclMembership``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.document_acl_condition_list
    import capo_bedrock_agent_runtime.types.document_acl_member_relation


class DocumentAclMembership(TypedDict, closed=True):
    member_relation: NotRequired[
        "capo_bedrock_agent_runtime.types.document_acl_member_relation.DocumentAclMemberRelation"
    ]
    """<p>The logical relation between conditions. Valid values: <code>AND</code> – All conditions must match. <code>OR</code> – At least one condition must match.</p>"""
    conditions: NotRequired[
        "capo_bedrock_agent_runtime.types.document_acl_condition_list.DocumentAclConditionList"
    ]
    """<p>The list of conditions that determine membership.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAclMembership) -> dict:
    out: dict = {}
    if "member_relation" in value:
        import capo_bedrock_agent_runtime.types.document_acl_member_relation

        out["memberRelation"] = (
            capo_bedrock_agent_runtime.types.document_acl_member_relation.serialize_json(
                value["member_relation"]
            )
        )
    if "conditions" in value:
        import capo_bedrock_agent_runtime.types.document_acl_condition_list

        out["conditions"] = (
            capo_bedrock_agent_runtime.types.document_acl_condition_list.serialize_json(
                value["conditions"]
            )
        )
    return out


def deserialize_json(data: dict) -> DocumentAclMembership:
    out: DocumentAclMembership = {}  # type: ignore[typeddict-item]
    if data.get("memberRelation") is not None:
        import capo_bedrock_agent_runtime.types.document_acl_member_relation

        out["member_relation"] = (
            capo_bedrock_agent_runtime.types.document_acl_member_relation.deserialize_json(
                data["memberRelation"]
            )
        )
    if data.get("conditions") is not None:
        import capo_bedrock_agent_runtime.types.document_acl_condition_list

        out["conditions"] = (
            capo_bedrock_agent_runtime.types.document_acl_condition_list.deserialize_json(
                data["conditions"]
            )
        )
    return out
