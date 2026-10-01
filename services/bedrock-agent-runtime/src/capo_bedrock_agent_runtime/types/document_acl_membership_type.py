"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#DocumentAclMembershipType``."""

from typing import Literal, TypeAlias, cast

"""<p>The scope type for a document access control list (ACL) membership condition. Valid values: <code>KNOWLEDGE_BASE</code> – The entry applies at the knowledge base level. <code>DATA_SOURCE</code> – The entry applies at the data source level.</p>"""
DocumentAclMembershipType: TypeAlias = Literal[
    "KNOWLEDGE_BASE",
    "DATA_SOURCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAclMembershipType) -> str:
    return value


def deserialize_json(data: str) -> DocumentAclMembershipType:
    return cast(DocumentAclMembershipType, data)
