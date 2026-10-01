"""Generated from Smithy shape ``com.amazonaws.securityhub#ScopeType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of scope for an Azure connector. Valid values are <code>TENANT</code> (monitor all subscriptions in the tenant) and <code>SUBSCRIPTION</code> (monitor specific subscriptions).</p>"""
ScopeType: TypeAlias = Literal[
    "TENANT",
    "SUBSCRIPTION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScopeType) -> str:
    return value


def deserialize_json(data: str) -> ScopeType:
    return cast(ScopeType, data)
