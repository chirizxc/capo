"""Generated from Smithy shape ``com.amazonaws.swf#ActivityTaskCompletedEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.data
    import capo_swf.types.event_id


class ActivityTaskCompletedEventAttributes(TypedDict, closed=True):
    result: NotRequired["capo_swf.types.data.Data"]
    """<p>The results of the activity task.</p>"""
    scheduled_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>ActivityTaskScheduled</code> event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""
    started_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>ActivityTaskStarted</code> event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityTaskCompletedEventAttributes) -> dict:
    out: dict = {}
    if "result" in value:
        out["result"] = value["result"]
    out["scheduledEventId"] = value.get("scheduled_event_id", 0)
    out["startedEventId"] = value.get("started_event_id", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> ActivityTaskCompletedEventAttributes:
    out: ActivityTaskCompletedEventAttributes = {}  # type: ignore[typeddict-item]
    if data.get("result") is not None:
        out["result"] = data["result"]
    if data.get("scheduledEventId") is not None:
        out["scheduled_event_id"] = data["scheduledEventId"]
    else:
        out["scheduled_event_id"] = 0
    if data.get("startedEventId") is not None:
        out["started_event_id"] = data["startedEventId"]
    else:
        out["started_event_id"] = 0
    return out
