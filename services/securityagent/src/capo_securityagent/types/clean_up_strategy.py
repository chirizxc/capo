"""Generated from Smithy shape ``com.amazonaws.securityagent#CleanUpStrategy``."""

from typing import Literal, TypeAlias, cast

"""<p>Strategy for handling resources created during a pentest.</p>"""
CleanUpStrategy: TypeAlias = Literal[
    "BEST_EFFORT_DELETE",
    "RETAIN_ALL",
]


# --- restJson1 ser/de ---
def serialize_json(value: CleanUpStrategy) -> str:
    return value


def deserialize_json(data: str) -> CleanUpStrategy:
    return cast(CleanUpStrategy, data)
