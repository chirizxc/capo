"""Generated from Smithy shape ``com.amazonaws.iotsitewise#FailedDataSegmentDisassociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.failed_data_segment_disassociation

FailedDataSegmentDisassociations: TypeAlias = list[
    "capo_iotsitewise.types.failed_data_segment_disassociation.FailedDataSegmentDisassociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailedDataSegmentDisassociations) -> list:
    import capo_iotsitewise.types.failed_data_segment_disassociation

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.failed_data_segment_disassociation.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FailedDataSegmentDisassociations:
    import capo_iotsitewise.types.failed_data_segment_disassociation

    out: FailedDataSegmentDisassociations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_iotsitewise.types.failed_data_segment_disassociation.deserialize_json(
                item
            )
        )
    return out
