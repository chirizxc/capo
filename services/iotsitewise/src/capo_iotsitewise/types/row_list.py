"""Generated from Smithy shape ``com.amazonaws.iotsitewise#RowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.result

RowList: TypeAlias = list["capo_iotsitewise.types.result.Result"]


# --- restJson1 ser/de ---
def serialize_json(value: RowList) -> list:
    import capo_iotsitewise.types.result

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.result.serialize_json(item))
    return out


def deserialize_json(data: list) -> RowList:
    import capo_iotsitewise.types.result

    out: RowList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iotsitewise.types.result.deserialize_json(item))
    return out
