"""Generated from Smithy shape ``com.amazonaws.iotsitewise#TimeseriesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.timeseries_item

TimeseriesList: TypeAlias = list[
    "capo_iotsitewise.types.timeseries_item.TimeseriesItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeseriesList) -> list:
    import capo_iotsitewise.types.timeseries_item

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.timeseries_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> TimeseriesList:
    import capo_iotsitewise.types.timeseries_item

    out: TimeseriesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iotsitewise.types.timeseries_item.deserialize_json(item))
    return out
