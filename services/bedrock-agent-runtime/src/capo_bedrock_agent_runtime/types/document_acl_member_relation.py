"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#DocumentAclMemberRelation``."""

from typing import Literal, TypeAlias, cast

"""<p>The logical relation for combining access control list (ACL) membership conditions.</p>"""
DocumentAclMemberRelation: TypeAlias = Literal[
    "AND",
    "OR",
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAclMemberRelation) -> str:
    return value


def deserialize_json(data: str) -> DocumentAclMemberRelation:
    return cast(DocumentAclMemberRelation, data)
