"""Generated from Smithy shape ``com.amazonaws.securityagent#ThreatStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Status of a threat.</p>"""
ThreatStatus: TypeAlias = Literal[
    "OPEN",
    "RESOLVED",
    "DISMISSED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatStatus) -> str:
    return value


def deserialize_json(data: str) -> ThreatStatus:
    return cast(ThreatStatus, data)
