"""Generated from Smithy shape ``com.amazonaws.quicksight#CapabilityState``."""

from typing import Literal, TypeAlias, cast

"""<p>The permission state of a capability in a custom permissions profile. Valid values:</p> <ul> <li> <p> <code>DENY</code> – Amazon Quick denies this capability for users assigned to the profile.</p> </li> <li> <p> <code>ALLOW</code> – Amazon Quick grants this capability to users assigned to the profile. This value is only relevant when governance is enabled for the capability's category. Without governance, the default effect is always <code>ALLOW</code>. In a governed category, this value overrides the category-level deny-by-default behavior for that capability only.</p> </li> </ul>"""
CapabilityState: TypeAlias = Literal[
    "DENY",
    "ALLOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityState) -> str:
    return value


def deserialize_json(data: str) -> CapabilityState:
    return cast(CapabilityState, data)
