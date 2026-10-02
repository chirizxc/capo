"""Generated from Smithy shape ``com.amazonaws.iotsitewise#SearchFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.data_set_id_list
    import capo_iotsitewise.types.time_interval_list
    import capo_iotsitewise.types.time_series_id_list


class SearchFilters(TypedDict, closed=True):
    time_series_ids: NotRequired[
        "capo_iotsitewise.types.time_series_id_list.TimeSeriesIdList"
    ]
    """<p>Restricts the search to these time series.</p>"""
    dataset_ids: NotRequired["capo_iotsitewise.types.data_set_id_list.DataSetIdList"]
    """<p>Restricts the search to these datasets.</p>"""
    time_intervals: NotRequired[
        "capo_iotsitewise.types.time_interval_list.TimeIntervalList"
    ]
    """<p>Restricts the search to these time intervals.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchFilters) -> dict:
    out: dict = {}
    if "time_series_ids" in value:
        import capo_iotsitewise.types.time_series_id_list

        out["timeSeriesIds"] = (
            capo_iotsitewise.types.time_series_id_list.serialize_json(
                value["time_series_ids"]
            )
        )
    if "dataset_ids" in value:
        import capo_iotsitewise.types.data_set_id_list

        out["datasetIds"] = capo_iotsitewise.types.data_set_id_list.serialize_json(
            value["dataset_ids"]
        )
    if "time_intervals" in value:
        import capo_iotsitewise.types.time_interval_list

        out["timeIntervals"] = capo_iotsitewise.types.time_interval_list.serialize_json(
            value["time_intervals"]
        )
    return out


def deserialize_json(data: dict) -> SearchFilters:
    out: SearchFilters = {}  # type: ignore[typeddict-item]
    if data.get("timeSeriesIds") is not None:
        import capo_iotsitewise.types.time_series_id_list

        out["time_series_ids"] = (
            capo_iotsitewise.types.time_series_id_list.deserialize_json(
                data["timeSeriesIds"]
            )
        )
    if data.get("datasetIds") is not None:
        import capo_iotsitewise.types.data_set_id_list

        out["dataset_ids"] = capo_iotsitewise.types.data_set_id_list.deserialize_json(
            data["datasetIds"]
        )
    if data.get("timeIntervals") is not None:
        import capo_iotsitewise.types.time_interval_list

        out["time_intervals"] = (
            capo_iotsitewise.types.time_interval_list.deserialize_json(
                data["timeIntervals"]
            )
        )
    return out
