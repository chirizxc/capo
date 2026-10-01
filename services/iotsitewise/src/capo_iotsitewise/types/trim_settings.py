"""Generated from Smithy shape ``com.amazonaws.iotsitewise#TrimSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.time_in_nanos


class TrimSettings(TypedDict, closed=True):
    start_time: "capo_iotsitewise.types.time_in_nanos.TimeInNanos"
    """<p>The start time for the trim range.</p>"""
    end_time: "capo_iotsitewise.types.time_in_nanos.TimeInNanos"
    """<p>The end time for the trim range. Must be greater than startTime.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrimSettings) -> dict:
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


def deserialize_json(data: dict) -> TrimSettings:
    out: TrimSettings = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        import capo_iotsitewise.types.time_in_nanos

        out["start_time"] = capo_iotsitewise.types.time_in_nanos.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("TrimSettings.start_time required")
    if data.get("endTime") is not None:
        import capo_iotsitewise.types.time_in_nanos

        out["end_time"] = capo_iotsitewise.types.time_in_nanos.deserialize_json(
            data["endTime"]
        )
    else:
        raise DeserializationError("TrimSettings.end_time required")
    return out
