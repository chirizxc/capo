"""Generated from Smithy shape ``com.amazonaws.iotsitewise#FailedDataSegmentDeletions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.failed_data_segment_deletion

FailedDataSegmentDeletions: TypeAlias = list[
    "capo_iotsitewise.types.failed_data_segment_deletion.FailedDataSegmentDeletion"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailedDataSegmentDeletions) -> list:
    import capo_iotsitewise.types.failed_data_segment_deletion

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.failed_data_segment_deletion.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FailedDataSegmentDeletions:
    import capo_iotsitewise.types.failed_data_segment_deletion

    out: FailedDataSegmentDeletions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_iotsitewise.types.failed_data_segment_deletion.deserialize_json(item)
        )
    return out
