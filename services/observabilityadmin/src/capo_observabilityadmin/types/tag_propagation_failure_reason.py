"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TagPropagationFailureReason``."""

from typing import Literal, TypeAlias, cast

"""<p>The reason tag propagation is unhealthy for a centralization rule.</p> <ul> <li> <p> <code>RoleNotAssumable</code> – The service cannot assume the destination role due to a trust policy or external ID misconfiguration.</p> </li> <li> <p> <code>RoleLacksPermissions</code> – The role was assumed successfully but the tag API call was denied by the role's permissions policy.</p> </li> </ul>"""
TagPropagationFailureReason: TypeAlias = Literal[
    "RoleNotAssumable",
    "RoleLacksPermissions",
]


# --- restJson1 ser/de ---
def serialize_json(value: TagPropagationFailureReason) -> str:
    return value


def deserialize_json(data: str) -> TagPropagationFailureReason:
    return cast(TagPropagationFailureReason, data)
