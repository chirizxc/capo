"""Generated from Smithy shape ``com.amazonaws.iotsitewise#SearchStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The lifecycle status of a search.</p>"""
SearchStatus: TypeAlias = Literal[
    "QUEUED",
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchStatus) -> str:
    return value


def deserialize_json(data: str) -> SearchStatus:
    return cast(SearchStatus, data)
