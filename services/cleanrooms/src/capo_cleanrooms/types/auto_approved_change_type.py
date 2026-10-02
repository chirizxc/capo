"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AutoApprovedChangeType``."""

from typing import Literal, TypeAlias, cast

AutoApprovedChangeType: TypeAlias = Literal[
    "ADD_MEMBER",
    "GRANT_RECEIVE_RESULTS_ABILITY",
    "REVOKE_RECEIVE_RESULTS_ABILITY",
    "GRANT_EXPORT_QUERY_ANALYSIS_LOG_ABILITY",
    "REVOKE_EXPORT_QUERY_ANALYSIS_LOG_ABILITY",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoApprovedChangeType) -> str:
    return value


def deserialize_json(data: str) -> AutoApprovedChangeType:
    return cast(AutoApprovedChangeType, data)
