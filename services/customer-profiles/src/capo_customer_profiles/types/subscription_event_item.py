"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SubscriptionEventItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.subscription_event
    import capo_customer_profiles.types.subscription_event_type
    import capo_customer_profiles.types.timestamp
    import capo_customer_profiles.types.uuid


class SubscriptionEventItem(TypedDict, closed=True):
    profile_id: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>The unique identifier of a customer profile.</p>"""
    updated_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the membership change was detected. </p>"""
    event_type: NotRequired[
        "capo_customer_profiles.types.subscription_event_type.SubscriptionEventType"
    ]
    """<p>The type of event that triggered the membership change. The following are valid values: </p> <ul> <li> <p> <b>LIVE</b>: Real-time event triggered by a profile or calculated attribute change (Classic segments only). </p> </li> <li> <p> <b>SCHEDULE</b>: Event generated during a scheduled execution. </p> </li> </ul>"""
    event: NotRequired[
        "capo_customer_profiles.types.subscription_event.SubscriptionEvent"
    ]
    """<p>Whether the profile joined or left the segment. The following are valid values: </p> <ul> <li> <p> <b>JOINED</b>: The profile joined the segment. </p> </li> <li> <p> <b>LEFT</b>: The profile left the segment. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionEventItem) -> dict:
    out: dict = {}
    if "profile_id" in value:
        out["ProfileId"] = value["profile_id"]
    if "updated_at" in value:
        import capo_customer_profiles.types.timestamp

        out["UpdatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "event_type" in value:
        import capo_customer_profiles.types.subscription_event_type

        out["EventType"] = (
            capo_customer_profiles.types.subscription_event_type.serialize_json(
                value["event_type"]
            )
        )
    if "event" in value:
        import capo_customer_profiles.types.subscription_event

        out["Event"] = capo_customer_profiles.types.subscription_event.serialize_json(
            value["event"]
        )
    return out


def deserialize_json(data: dict) -> SubscriptionEventItem:
    out: SubscriptionEventItem = {}  # type: ignore[typeddict-item]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    if data.get("UpdatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["updated_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if data.get("EventType") is not None:
        import capo_customer_profiles.types.subscription_event_type

        out["event_type"] = (
            capo_customer_profiles.types.subscription_event_type.deserialize_json(
                data["EventType"]
            )
        )
    if data.get("Event") is not None:
        import capo_customer_profiles.types.subscription_event

        out["event"] = capo_customer_profiles.types.subscription_event.deserialize_json(
            data["Event"]
        )
    return out
