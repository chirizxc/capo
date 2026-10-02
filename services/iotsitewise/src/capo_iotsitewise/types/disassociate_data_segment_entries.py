"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DisassociateDataSegmentEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.disassociate_data_segment_entry

DisassociateDataSegmentEntries: TypeAlias = list[
    "capo_iotsitewise.types.disassociate_data_segment_entry.DisassociateDataSegmentEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateDataSegmentEntries) -> list:
    import capo_iotsitewise.types.disassociate_data_segment_entry

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.disassociate_data_segment_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DisassociateDataSegmentEntries:
    import capo_iotsitewise.types.disassociate_data_segment_entry

    out: DisassociateDataSegmentEntries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_iotsitewise.types.disassociate_data_segment_entry.deserialize_json(
                item
            )
        )
    return out
