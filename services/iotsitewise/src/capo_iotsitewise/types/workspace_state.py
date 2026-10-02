"""Generated from Smithy shape ``com.amazonaws.iotsitewise#WorkspaceState``."""

from typing import Literal, TypeAlias, cast

"""<p>The current state of a workspace. The state changes as the workspace is created, updated, or deleted.</p>"""
WorkspaceState: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceState) -> str:
    return value


def deserialize_json(data: str) -> WorkspaceState:
    return cast(WorkspaceState, data)
