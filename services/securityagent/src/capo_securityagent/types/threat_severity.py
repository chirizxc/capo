"""Generated from Smithy shape ``com.amazonaws.securityagent#ThreatSeverity``."""

from typing import Literal, TypeAlias, cast

"""<p>Severity level for a threat.</p>"""
ThreatSeverity: TypeAlias = Literal[
    "CRITICAL",
    "HIGH",
    "MEDIUM",
    "LOW",
    "INFO",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatSeverity) -> str:
    return value


def deserialize_json(data: str) -> ThreatSeverity:
    return cast(ThreatSeverity, data)
