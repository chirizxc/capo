"""Generated from Smithy shape ``com.amazonaws.securityagent#ThreatActor``."""

from typing import Literal, TypeAlias, cast

"""<p>Indicates whether a threat was created or updated by a customer or an agent.</p>"""
ThreatActor: TypeAlias = Literal[
    "CUSTOMER",
    "AGENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatActor) -> str:
    return value


def deserialize_json(data: str) -> ThreatActor:
    return cast(ThreatActor, data)
