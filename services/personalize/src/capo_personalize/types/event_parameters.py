"""Generated from Smithy shape ``com.amazonaws.personalize#EventParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.event_type
    import capo_personalize.types.event_type_threshold_value
    import capo_personalize.types.event_type_weight


class EventParameters(TypedDict, closed=True):
    event_type: NotRequired["capo_personalize.types.event_type.EventType"]
    """<p>The name of the event type to be considered for solution creation.</p>"""
    event_value_threshold: NotRequired[
        "capo_personalize.types.event_type_threshold_value.EventTypeThresholdValue"
    ]
    """<p>The threshold of the event type. Only events with a value greater or equal to this threshold will be considered for solution creation.</p>"""
    weight: NotRequired["capo_personalize.types.event_type_weight.EventTypeWeight"]
    """<p>The weight of the event type. A higher weight means higher importance of the event type for the created solution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventParameters) -> dict:
    out: dict = {}
    if "event_type" in value:
        out["eventType"] = value["event_type"]
    if "event_value_threshold" in value:
        out["eventValueThreshold"] = (
            "NaN"
            if value["event_value_threshold"] != value["event_value_threshold"]
            else "Infinity"
            if value["event_value_threshold"] == float("inf")
            else "-Infinity"
            if value["event_value_threshold"] == float("-inf")
            else value["event_value_threshold"]
        )
    if "weight" in value:
        out["weight"] = (
            "NaN"
            if value["weight"] != value["weight"]
            else "Infinity"
            if value["weight"] == float("inf")
            else "-Infinity"
            if value["weight"] == float("-inf")
            else value["weight"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EventParameters:
    out: EventParameters = {}  # type: ignore[typeddict-item]
    if data.get("eventType") is not None:
        out["event_type"] = data["eventType"]
    if data.get("eventValueThreshold") is not None:
        out["event_value_threshold"] = float(data["eventValueThreshold"])
    if data.get("weight") is not None:
        out["weight"] = float(data["weight"])
    return out
