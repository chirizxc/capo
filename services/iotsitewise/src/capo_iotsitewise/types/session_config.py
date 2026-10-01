"""Generated from Smithy shape ``com.amazonaws.iotsitewise#SessionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.time_in_nanos


class SessionConfig(TypedDict, closed=True):
    session_start_timestamp: "capo_iotsitewise.types.time_in_nanos.TimeInNanos"
    """<p>The nanosecond-precision start time of the session.</p>"""
    session_end_timestamp: "capo_iotsitewise.types.time_in_nanos.TimeInNanos"
    """<p>The nanosecond-precision end time of the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionConfig) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.time_in_nanos

    out["sessionStartTimestamp"] = capo_iotsitewise.types.time_in_nanos.serialize_json(
        value["session_start_timestamp"]
    )
    import capo_iotsitewise.types.time_in_nanos

    out["sessionEndTimestamp"] = capo_iotsitewise.types.time_in_nanos.serialize_json(
        value["session_end_timestamp"]
    )
    return out


def deserialize_json(data: dict) -> SessionConfig:
    out: SessionConfig = {}  # type: ignore[typeddict-item]
    if data.get("sessionStartTimestamp") is not None:
        import capo_iotsitewise.types.time_in_nanos

        out["session_start_timestamp"] = (
            capo_iotsitewise.types.time_in_nanos.deserialize_json(
                data["sessionStartTimestamp"]
            )
        )
    else:
        raise DeserializationError("SessionConfig.session_start_timestamp required")
    if data.get("sessionEndTimestamp") is not None:
        import capo_iotsitewise.types.time_in_nanos

        out["session_end_timestamp"] = (
            capo_iotsitewise.types.time_in_nanos.deserialize_json(
                data["sessionEndTimestamp"]
            )
        )
    else:
        raise DeserializationError("SessionConfig.session_end_timestamp required")
    return out
