"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#DocumentAclUser``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.document_acl_membership_type


class DocumentAclUser(TypedDict, closed=True):
    id: "str"
    """<p>The identifier of the user.</p>"""
    type: "capo_bedrock_agent_runtime.types.document_acl_membership_type.DocumentAclMembershipType"
    """<p>The membership type indicating the scope of the user entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAclUser) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_bedrock_agent_runtime.types.document_acl_membership_type

    out["type"] = (
        capo_bedrock_agent_runtime.types.document_acl_membership_type.serialize_json(
            value["type"]
        )
    )
    return out


def deserialize_json(data: dict) -> DocumentAclUser:
    out: DocumentAclUser = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DocumentAclUser.id required")
    if data.get("type") is not None:
        import capo_bedrock_agent_runtime.types.document_acl_membership_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.document_acl_membership_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("DocumentAclUser.type required")
    return out
