"""Generated from Smithy shape ``com.amazonaws.iotsitewise#TimeseriesItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_property_alias
    import capo_iotsitewise.types.format_settings
    import capo_iotsitewise.types.time_series_id
    import capo_iotsitewise.types.trim_settings


class TimeseriesItem(TypedDict, closed=True):
    time_series_id: NotRequired["capo_iotsitewise.types.time_series_id.TimeSeriesId"]
    """<p>The unique identifier for the timeseries. Mutually exclusive with propertyAlias.</p>"""
    property_alias: NotRequired[
        "capo_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
    ]
    """<p>The customer-friendly alias for the timeseries. Mutually exclusive with timeSeriesId.</p>"""
    trim_settings: NotRequired["capo_iotsitewise.types.trim_settings.TrimSettings"]
    """<p>The trim settings for the time range to export. Required for VIDEO and TELEMETRY data types; optional for ANNOTATION data types.</p>"""
    format_settings: NotRequired[
        "capo_iotsitewise.types.format_settings.FormatSettings"
    ]
    """<p>The optional format settings for the output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeseriesItem) -> dict:
    out: dict = {}
    if "time_series_id" in value:
        out["timeSeriesId"] = value["time_series_id"]
    if "property_alias" in value:
        out["propertyAlias"] = value["property_alias"]
    if "trim_settings" in value:
        import capo_iotsitewise.types.trim_settings

        out["trimSettings"] = capo_iotsitewise.types.trim_settings.serialize_json(
            value["trim_settings"]
        )
    if "format_settings" in value:
        import capo_iotsitewise.types.format_settings

        out["formatSettings"] = capo_iotsitewise.types.format_settings.serialize_json(
            value["format_settings"]
        )
    return out


def deserialize_json(data: dict) -> TimeseriesItem:
    out: TimeseriesItem = {}  # type: ignore[typeddict-item]
    if data.get("timeSeriesId") is not None:
        out["time_series_id"] = data["timeSeriesId"]
    if data.get("propertyAlias") is not None:
        out["property_alias"] = data["propertyAlias"]
    if data.get("trimSettings") is not None:
        import capo_iotsitewise.types.trim_settings

        out["trim_settings"] = capo_iotsitewise.types.trim_settings.deserialize_json(
            data["trimSettings"]
        )
    if data.get("formatSettings") is not None:
        import capo_iotsitewise.types.format_settings

        out["format_settings"] = (
            capo_iotsitewise.types.format_settings.deserialize_json(
                data["formatSettings"]
            )
        )
    return out
