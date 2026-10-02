"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ApplicationStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Current status of the application</p>"""
ApplicationStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationStatus) -> str:
    return value


def deserialize_json(data: str) -> ApplicationStatus:
    return cast(ApplicationStatus, data)
