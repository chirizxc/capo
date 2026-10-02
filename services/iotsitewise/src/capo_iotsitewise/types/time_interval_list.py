"""Generated from Smithy shape ``com.amazonaws.iotsitewise#TimeIntervalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.time_interval

TimeIntervalList: TypeAlias = list["capo_iotsitewise.types.time_interval.TimeInterval"]


# --- restJson1 ser/de ---
def serialize_json(value: TimeIntervalList) -> list:
    import capo_iotsitewise.types.time_interval

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.time_interval.serialize_json(item))
    return out


def deserialize_json(data: list) -> TimeIntervalList:
    import capo_iotsitewise.types.time_interval

    out: TimeIntervalList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iotsitewise.types.time_interval.deserialize_json(item))
    return out
