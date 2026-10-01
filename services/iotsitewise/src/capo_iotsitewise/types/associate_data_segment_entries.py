"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssociateDataSegmentEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.associate_data_segment_entry

AssociateDataSegmentEntries: TypeAlias = list[
    "capo_iotsitewise.types.associate_data_segment_entry.AssociateDataSegmentEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociateDataSegmentEntries) -> list:
    import capo_iotsitewise.types.associate_data_segment_entry

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.associate_data_segment_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssociateDataSegmentEntries:
    import capo_iotsitewise.types.associate_data_segment_entry

    out: AssociateDataSegmentEntries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_iotsitewise.types.associate_data_segment_entry.deserialize_json(item)
        )
    return out
