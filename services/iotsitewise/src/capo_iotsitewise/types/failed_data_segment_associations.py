"""Generated from Smithy shape ``com.amazonaws.iotsitewise#FailedDataSegmentAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.failed_data_segment_association

FailedDataSegmentAssociations: TypeAlias = list[
    "capo_iotsitewise.types.failed_data_segment_association.FailedDataSegmentAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailedDataSegmentAssociations) -> list:
    import capo_iotsitewise.types.failed_data_segment_association

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.failed_data_segment_association.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FailedDataSegmentAssociations:
    import capo_iotsitewise.types.failed_data_segment_association

    out: FailedDataSegmentAssociations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_iotsitewise.types.failed_data_segment_association.deserialize_json(
                item
            )
        )
    return out
