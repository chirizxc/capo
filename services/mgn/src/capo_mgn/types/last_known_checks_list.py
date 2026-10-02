"""Generated from Smithy shape ``com.amazonaws.mgn#LastKnownChecksList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.last_known_check

LastKnownChecksList: TypeAlias = list["capo_mgn.types.last_known_check.LastKnownCheck"]


# --- restJson1 ser/de ---
def serialize_json(value: LastKnownChecksList) -> list:
    import capo_mgn.types.last_known_check

    out: list = []
    for item in value:
        out.append(capo_mgn.types.last_known_check.serialize_json(item))
    return out


def deserialize_json(data: list) -> LastKnownChecksList:
    import capo_mgn.types.last_known_check

    out: LastKnownChecksList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mgn.types.last_known_check.deserialize_json(item))
    return out
