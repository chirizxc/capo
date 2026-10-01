"""Generated from Smithy shape ``com.amazonaws.iotsitewise#TimeSeriesIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.time_series_id

TimeSeriesIdList: TypeAlias = list["capo_iotsitewise.types.time_series_id.TimeSeriesId"]


# --- restJson1 ser/de ---
def serialize_json(value: TimeSeriesIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> TimeSeriesIdList:
    return [item for item in data if item is not None]
