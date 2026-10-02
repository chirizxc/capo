"""Generated from Smithy shape ``com.amazonaws.iotsitewise#TimeInterval``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.time_in_nanos


class TimeInterval(TypedDict, closed=True):
    start_time: "capo_iotsitewise.types.time_in_nanos.TimeInNanos"
    """<p>The start of the time interval.</p>"""
    end_time: "capo_iotsitewise.types.time_in_nanos.TimeInNanos"
    """<p>The end of the time interval.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeInterval) -> dict:
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


def deserialize_json(data: dict) -> TimeInterval:
    out: TimeInterval = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        import capo_iotsitewise.types.time_in_nanos

        out["start_time"] = capo_iotsitewise.types.time_in_nanos.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("TimeInterval.start_time required")
    if data.get("endTime") is not None:
        import capo_iotsitewise.types.time_in_nanos

        out["end_time"] = capo_iotsitewise.types.time_in_nanos.deserialize_json(
            data["endTime"]
        )
    else:
        raise DeserializationError("TimeInterval.end_time required")
    return out
