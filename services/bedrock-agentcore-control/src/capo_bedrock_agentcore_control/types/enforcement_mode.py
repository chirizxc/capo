"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EnforcementMode``."""

from typing import Literal, TypeAlias, cast

"""<p>The enforcement mode for a policy. Run this policy in <code>LOG_ONLY</code> mode to collect data on how it affects your application. Once you are satisfied with the data gathered, switch the policy to <code>ACTIVE</code>.</p>"""
EnforcementMode: TypeAlias = Literal[
    "ACTIVE",
    "LOG_ONLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: EnforcementMode) -> str:
    return value


def deserialize_json(data: str) -> EnforcementMode:
    return cast(EnforcementMode, data)
