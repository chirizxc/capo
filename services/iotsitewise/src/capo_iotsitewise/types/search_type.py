"""Generated from Smithy shape ``com.amazonaws.iotsitewise#SearchType``."""

from typing import Literal, TypeAlias, cast

"""<p>The search strategy, which trades off latency against recall. <code>DEEP</code> runs the full semantic and structured search for the highest-quality matches; <code>QUICK</code> returns faster, lower-recall results. When <code>searchType</code> is omitted on a request, the search defaults to <code>QUICK</code>.</p>"""
SearchType: TypeAlias = Literal[
    "DEEP",
    "QUICK",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchType) -> str:
    return value


def deserialize_json(data: str) -> SearchType:
    return cast(SearchType, data)
