"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AccessControlPrincipalType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of principal in an access control entry.</p>"""
AccessControlPrincipalType: TypeAlias = Literal["USER",]


# --- restJson1 ser/de ---
def serialize_json(value: AccessControlPrincipalType) -> str:
    return value


def deserialize_json(data: str) -> AccessControlPrincipalType:
    return cast(AccessControlPrincipalType, data)
