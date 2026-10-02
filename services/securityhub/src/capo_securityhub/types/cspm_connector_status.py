"""Generated from Smithy shape ``com.amazonaws.securityhub#CspmConnectorStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The connectivity status of a CSPM connector.</p>"""
CspmConnectorStatus: TypeAlias = Literal[
    "CONNECTED",
    "DEGRADED",
    "FAILED_TO_CONNECT",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: CspmConnectorStatus) -> str:
    return value


def deserialize_json(data: str) -> CspmConnectorStatus:
    return cast(CspmConnectorStatus, data)
