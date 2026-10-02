"""Generated from Smithy shape ``com.amazonaws.iotsitewise#QueryStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a query execution.</p>"""
QueryStatus: TypeAlias = Literal[
    "SUBMITTED",
    "RUNNING",
    "COMPLETED",
    "FAILED",
    "CANCELED",
    "CANCELING",
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryStatus) -> str:
    return value


def deserialize_json(data: str) -> QueryStatus:
    return cast(QueryStatus, data)
