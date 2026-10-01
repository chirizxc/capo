"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ColumnInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.column_information

ColumnInformationList: TypeAlias = list[
    "capo_iotsitewise.types.column_information.ColumnInformation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnInformationList) -> list:
    import capo_iotsitewise.types.column_information

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.column_information.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnInformationList:
    import capo_iotsitewise.types.column_information

    out: ColumnInformationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iotsitewise.types.column_information.deserialize_json(item))
    return out
