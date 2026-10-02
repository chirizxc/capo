"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeleteDataSegmentEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.delete_data_segment_entry

DeleteDataSegmentEntries: TypeAlias = list[
    "capo_iotsitewise.types.delete_data_segment_entry.DeleteDataSegmentEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataSegmentEntries) -> list:
    import capo_iotsitewise.types.delete_data_segment_entry

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.delete_data_segment_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DeleteDataSegmentEntries:
    import capo_iotsitewise.types.delete_data_segment_entry

    out: DeleteDataSegmentEntries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_iotsitewise.types.delete_data_segment_entry.deserialize_json(item)
        )
    return out
