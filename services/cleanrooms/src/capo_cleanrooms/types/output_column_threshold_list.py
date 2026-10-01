"""Generated from Smithy shape ``com.amazonaws.cleanrooms#OutputColumnThresholdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.output_column_threshold

OutputColumnThresholdList: TypeAlias = list[
    "capo_cleanrooms.types.output_column_threshold.OutputColumnThreshold"
]


# --- restJson1 ser/de ---
def serialize_json(value: OutputColumnThresholdList) -> list:
    import capo_cleanrooms.types.output_column_threshold

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.output_column_threshold.serialize_json(item))
    return out


def deserialize_json(data: list) -> OutputColumnThresholdList:
    import capo_cleanrooms.types.output_column_threshold

    out: OutputColumnThresholdList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cleanrooms.types.output_column_threshold.deserialize_json(item))
    return out
