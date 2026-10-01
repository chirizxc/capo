"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunSourceEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.test_run_source_arn
    import capo_resiliencehubv2.types.test_run_source_event_detail
    import capo_resiliencehubv2.types.test_run_source_event_type


class TestRunSourceEvent(TypedDict, closed=True):
    timestamp: "datetime.datetime"
    """<p>The timestamp when the event occurred.</p>"""
    source_arn: "capo_resiliencehubv2.types.test_run_source_arn.TestRunSourceArn"
    """<p>The ARN of the monitoring source the event belongs to.</p>"""
    event_type: (
        "capo_resiliencehubv2.types.test_run_source_event_type.TestRunSourceEventType"
    )
    """<p>The type of the event. ALARM indicates an event from a CloudWatch alarm source; the detail member carries either the alarm state change or a collection error.</p>"""
    detail: "capo_resiliencehubv2.types.test_run_source_event_detail.TestRunSourceEventDetail"
    """<p>The event payload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestRunSourceEvent) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types._prelude.timestamp

    out["timestamp"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    out["sourceArn"] = value["source_arn"]
    import capo_resiliencehubv2.types.test_run_source_event_type

    out["eventType"] = (
        capo_resiliencehubv2.types.test_run_source_event_type.serialize_json(
            value["event_type"]
        )
    )
    import capo_resiliencehubv2.types.test_run_source_event_detail

    out["detail"] = (
        capo_resiliencehubv2.types.test_run_source_event_detail.serialize_json(
            value["detail"]
        )
    )
    return out


def deserialize_json(data: dict) -> TestRunSourceEvent:
    out: TestRunSourceEvent = {}  # type: ignore[typeddict-item]
    if data.get("timestamp") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["timestamp"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        raise DeserializationError("TestRunSourceEvent.timestamp required")
    if data.get("sourceArn") is not None:
        out["source_arn"] = data["sourceArn"]
    else:
        raise DeserializationError("TestRunSourceEvent.source_arn required")
    if data.get("eventType") is not None:
        import capo_resiliencehubv2.types.test_run_source_event_type

        out["event_type"] = (
            capo_resiliencehubv2.types.test_run_source_event_type.deserialize_json(
                data["eventType"]
            )
        )
    else:
        raise DeserializationError("TestRunSourceEvent.event_type required")
    if data.get("detail") is not None:
        import capo_resiliencehubv2.types.test_run_source_event_detail

        out["detail"] = (
            capo_resiliencehubv2.types.test_run_source_event_detail.deserialize_json(
                data["detail"]
            )
        )
    else:
        raise DeserializationError("TestRunSourceEvent.detail required")
    return out
