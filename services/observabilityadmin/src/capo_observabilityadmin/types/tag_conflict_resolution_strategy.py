"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TagConflictResolutionStrategy``."""

from typing import Literal, TypeAlias, cast

"""<p>The strategy for resolving tag conflicts between source and destination log groups.</p> <ul> <li> <p> <code>ADD_ONLY</code> – Only adds new tags from the source without modifying existing destination tags.</p> </li> <li> <p> <code>UPDATE_SYNC</code> – Adds new tags and updates existing tags from the source. Does not remove destination tags that are absent from the source.</p> </li> <li> <p> <code>IN_SYNC</code> – Keeps destination tags fully synchronized with source tags, including removing destination tags that do not exist on the source.</p> </li> </ul>"""
TagConflictResolutionStrategy: TypeAlias = Literal[
    "IN_SYNC",
    "ADD_ONLY",
    "UPDATE_SYNC",
]


# --- restJson1 ser/de ---
def serialize_json(value: TagConflictResolutionStrategy) -> str:
    return value


def deserialize_json(data: str) -> TagConflictResolutionStrategy:
    return cast(TagConflictResolutionStrategy, data)
