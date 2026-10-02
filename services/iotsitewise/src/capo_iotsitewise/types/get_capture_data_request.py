"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GetCaptureDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_property_alias
    import capo_iotsitewise.types.format_settings
    import capo_iotsitewise.types.get_capture_data_next_token
    import capo_iotsitewise.types.time_in_nanos
    import capo_iotsitewise.types.time_series_id
    import capo_iotsitewise.types.workspace_name


class GetCaptureDataRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace that contains the capture source.</p>"""
    start_time: "capo_iotsitewise.types.time_in_nanos.TimeInNanos"
    """<p>The start time for the video data range.</p>"""
    end_time: "capo_iotsitewise.types.time_in_nanos.TimeInNanos"
    """<p>The end time for the video data range. Must be greater than startTime.</p>"""
    time_series_id: NotRequired["capo_iotsitewise.types.time_series_id.TimeSeriesId"]
    """<p>The time series ID that identifies the capture source. Mutually exclusive with propertyAlias.</p>"""
    property_alias: NotRequired[
        "capo_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
    ]
    """<p>The property alias that identifies the capture source. Mutually exclusive with timeSeriesId.</p>"""
    format_settings: NotRequired[
        "capo_iotsitewise.types.format_settings.FormatSettings"
    ]
    """<p>The optional format settings for the output.</p>"""
    next_token: NotRequired[
        "capo_iotsitewise.types.get_capture_data_next_token.GetCaptureDataNextToken"
    ]
    """<p>The token from a previous response used to continue retrieving data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCaptureDataRequest) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.time_in_nanos

    out["startTime"] = capo_iotsitewise.types.time_in_nanos.serialize_json(
        value["start_time"]
    )
    import capo_iotsitewise.types.time_in_nanos

    out["endTime"] = capo_iotsitewise.types.time_in_nanos.serialize_json(
        value["end_time"]
    )
    if "time_series_id" in value:
        out["timeSeriesId"] = value["time_series_id"]
    if "property_alias" in value:
        out["propertyAlias"] = value["property_alias"]
    if "format_settings" in value:
        import capo_iotsitewise.types.format_settings

        out["formatSettings"] = capo_iotsitewise.types.format_settings.serialize_json(
            value["format_settings"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetCaptureDataRequest:
    out: GetCaptureDataRequest = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        import capo_iotsitewise.types.time_in_nanos

        out["start_time"] = capo_iotsitewise.types.time_in_nanos.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("GetCaptureDataRequest.start_time required")
    if data.get("endTime") is not None:
        import capo_iotsitewise.types.time_in_nanos

        out["end_time"] = capo_iotsitewise.types.time_in_nanos.deserialize_json(
            data["endTime"]
        )
    else:
        raise DeserializationError("GetCaptureDataRequest.end_time required")
    if data.get("timeSeriesId") is not None:
        out["time_series_id"] = data["timeSeriesId"]
    if data.get("propertyAlias") is not None:
        out["property_alias"] = data["propertyAlias"]
    if data.get("formatSettings") is not None:
        import capo_iotsitewise.types.format_settings

        out["format_settings"] = (
            capo_iotsitewise.types.format_settings.deserialize_json(
                data["formatSettings"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
