"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AccessControlAccess``."""

from typing import Literal, TypeAlias, cast

"""<p>The access level for an access control entry.</p>"""
AccessControlAccess: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessControlAccess) -> str:
    return value


def deserialize_json(data: str) -> AccessControlAccess:
    return cast(AccessControlAccess, data)
