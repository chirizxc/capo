"""Generated from Smithy shape ``com.amazonaws.iotsitewise#EnrichmentTrimSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.time_in_nanos


class EnrichmentTrimSettings(TypedDict, closed=True):
    start_time: "capo_iotsitewise.types.time_in_nanos.TimeInNanos"
    """<p>Start time for the video analysis time range in nanoseconds since Unix epoch (TimeInNanos format). Data segments at or after this time are included in the enrichment. Must be within the dataset's time bounds.</p> <p>Example (JavaScript): Date.parse('2024-01-01T00:00:00Z') * 1000000 Example (Python): int(datetime.timestamp() * 1e9)</p>"""
    end_time: "capo_iotsitewise.types.time_in_nanos.TimeInNanos"
    """<p>End time for the video analysis time range in nanoseconds since Unix epoch (TimeInNanos format). Data segments at or before this time are included in the enrichment. Must be greater than startTime and within the dataset's time bounds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnrichmentTrimSettings) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.time_in_nanos

    out["startTime"] = capo_iotsitewise.types.time_in_nanos.serialize_json(
        value["start_time"]
    )
    import capo_iotsitewise.types.time_in_nanos

    out["endTime"] = capo_iotsitewise.types.time_in_nanos.serialize_json(
        value["end_time"]
    )
    return out


def deserialize_json(data: dict) -> EnrichmentTrimSettings:
    out: EnrichmentTrimSettings = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        import capo_iotsitewise.types.time_in_nanos

        out["start_time"] = capo_iotsitewise.types.time_in_nanos.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("EnrichmentTrimSettings.start_time required")
    if data.get("endTime") is not None:
        import capo_iotsitewise.types.time_in_nanos

        out["end_time"] = capo_iotsitewise.types.time_in_nanos.deserialize_json(
            data["endTime"]
        )
    else:
        raise DeserializationError("EnrichmentTrimSettings.end_time required")
    return out
