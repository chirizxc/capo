"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ExportDataTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.export_data_type

ExportDataTypeList: TypeAlias = list[
    "capo_iotsitewise.types.export_data_type.ExportDataType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportDataTypeList) -> list:
    import capo_iotsitewise.types.export_data_type

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.export_data_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExportDataTypeList:
    import capo_iotsitewise.types.export_data_type

    out: ExportDataTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iotsitewise.types.export_data_type.deserialize_json(item))
    return out
