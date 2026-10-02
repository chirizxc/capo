"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DataSegmentSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.data_segment_summary

DataSegmentSummaries: TypeAlias = list[
    "capo_iotsitewise.types.data_segment_summary.DataSegmentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSegmentSummaries) -> list:
    import capo_iotsitewise.types.data_segment_summary

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.data_segment_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSegmentSummaries:
    import capo_iotsitewise.types.data_segment_summary

    out: DataSegmentSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iotsitewise.types.data_segment_summary.deserialize_json(item))
    return out
