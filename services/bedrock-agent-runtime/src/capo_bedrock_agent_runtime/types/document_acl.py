"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#DocumentAcl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.document_acl_membership


class DocumentAcl(TypedDict, closed=True):
    allow_list: NotRequired[
        "capo_bedrock_agent_runtime.types.document_acl_membership.DocumentAclMembership"
    ]
    """<p>The list of principals allowed access to the document.</p>"""
    deny_list: NotRequired[
        "capo_bedrock_agent_runtime.types.document_acl_membership.DocumentAclMembership"
    ]
    """<p>The list of principals denied access to the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAcl) -> dict:
    out: dict = {}
    if "allow_list" in value:
        import capo_bedrock_agent_runtime.types.document_acl_membership

        out["allowList"] = (
            capo_bedrock_agent_runtime.types.document_acl_membership.serialize_json(
                value["allow_list"]
            )
        )
    if "deny_list" in value:
        import capo_bedrock_agent_runtime.types.document_acl_membership

        out["denyList"] = (
            capo_bedrock_agent_runtime.types.document_acl_membership.serialize_json(
                value["deny_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> DocumentAcl:
    out: DocumentAcl = {}  # type: ignore[typeddict-item]
    if data.get("allowList") is not None:
        import capo_bedrock_agent_runtime.types.document_acl_membership

        out["allow_list"] = (
            capo_bedrock_agent_runtime.types.document_acl_membership.deserialize_json(
                data["allowList"]
            )
        )
    if data.get("denyList") is not None:
        import capo_bedrock_agent_runtime.types.document_acl_membership

        out["deny_list"] = (
            capo_bedrock_agent_runtime.types.document_acl_membership.deserialize_json(
                data["denyList"]
            )
        )
    return out
