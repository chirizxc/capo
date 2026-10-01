"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConsentPortalStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The lifecycle status of a consent portal.</p>"""
ConsentPortalStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "UPDATE_FAILED",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConsentPortalStatus) -> str:
    return value


def deserialize_json(data: str) -> ConsentPortalStatus:
    return cast(ConsentPortalStatus, data)
