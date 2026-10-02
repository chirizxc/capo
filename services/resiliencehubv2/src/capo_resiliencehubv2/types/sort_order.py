"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SortOrder``."""

from typing import Literal, TypeAlias, cast

"""<p>The order in which to sort results.</p>"""
SortOrder: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- restJson1 ser/de ---
def serialize_json(value: SortOrder) -> str:
    return value


def deserialize_json(data: str) -> SortOrder:
    return cast(SortOrder, data)
