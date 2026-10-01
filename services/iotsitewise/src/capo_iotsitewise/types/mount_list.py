"""Generated from Smithy shape ``com.amazonaws.iotsitewise#MountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.mount

MountList: TypeAlias = list["capo_iotsitewise.types.mount.Mount"]


# --- restJson1 ser/de ---
def serialize_json(value: MountList) -> list:
    import capo_iotsitewise.types.mount

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.mount.serialize_json(item))
    return out


def deserialize_json(data: list) -> MountList:
    import capo_iotsitewise.types.mount

    out: MountList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iotsitewise.types.mount.deserialize_json(item))
    return out
