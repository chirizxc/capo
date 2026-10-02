"""Generated from Smithy shape ``com.amazonaws.securityhub#CspmEnablementStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The enablement status of a CSPM connector. Indicates the lifecycle state of the connector resource.</p>"""
CspmEnablementStatus: TypeAlias = Literal[
    "ENABLED",
    "PENDING_ENABLEMENT",
    "PENDING_UPDATE",
    "PENDING_DELETION",
]


# --- restJson1 ser/de ---
def serialize_json(value: CspmEnablementStatus) -> str:
    return value


def deserialize_json(data: str) -> CspmEnablementStatus:
    return cast(CspmEnablementStatus, data)
