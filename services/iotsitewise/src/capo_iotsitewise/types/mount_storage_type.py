"""Generated from Smithy shape ``com.amazonaws.iotsitewise#MountStorageType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of storage used for a mount inside the container.</p>"""
MountStorageType: TypeAlias = Literal["SHARED_STORAGE",]


# --- restJson1 ser/de ---
def serialize_json(value: MountStorageType) -> str:
    return value


def deserialize_json(data: str) -> MountStorageType:
    return cast(MountStorageType, data)
