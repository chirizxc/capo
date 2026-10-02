"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightResponseStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of an insight response. Possible values are <code>SUCCESS</code> and <code>ERROR</code>.</p>"""
InsightResponseStatus: TypeAlias = Literal[
    "SUCCESS",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightResponseStatus) -> str:
    return value


def deserialize_json(data: str) -> InsightResponseStatus:
    return cast(InsightResponseStatus, data)
