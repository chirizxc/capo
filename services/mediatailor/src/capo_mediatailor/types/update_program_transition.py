"""Generated from Smithy shape ``com.amazonaws.mediatailor#UpdateProgramTransition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__long


class UpdateProgramTransition(TypedDict, closed=True):
    scheduled_start_time_millis: NotRequired["capo_mediatailor.types.__long.__long"]
    """<p>The date and time that the program is scheduled to start, in epoch milliseconds.</p>"""
    duration_millis: NotRequired["capo_mediatailor.types.__long.__long"]
    """<p>The duration of the live program in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProgramTransition) -> dict:
    out: dict = {}
    if "scheduled_start_time_millis" in value:
        out["ScheduledStartTimeMillis"] = value["scheduled_start_time_millis"]
    if "duration_millis" in value:
        out["DurationMillis"] = value["duration_millis"]
    return out


def deserialize_json(data: dict) -> UpdateProgramTransition:
    out: UpdateProgramTransition = {}  # type: ignore[typeddict-item]
    if data.get("ScheduledStartTimeMillis") is not None:
        out["scheduled_start_time_millis"] = data["ScheduledStartTimeMillis"]
    if data.get("DurationMillis") is not None:
        out["duration_millis"] = data["DurationMillis"]
    return out
