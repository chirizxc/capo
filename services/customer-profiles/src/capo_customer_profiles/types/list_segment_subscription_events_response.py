"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListSegmentSubscriptionEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.subscription_events_list
    import capo_customer_profiles.types.token


class ListSegmentSubscriptionEventsResponse(TypedDict, closed=True):
    events: NotRequired[
        "capo_customer_profiles.types.subscription_events_list.SubscriptionEventsList"
    ]
    """<p>A list of segment membership events. </p>"""
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>The pagination token to use to retrieve the next page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSegmentSubscriptionEventsResponse) -> dict:
    out: dict = {}
    if "events" in value:
        import capo_customer_profiles.types.subscription_events_list

        out["Events"] = (
            capo_customer_profiles.types.subscription_events_list.serialize_json(
                value["events"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSegmentSubscriptionEventsResponse:
    out: ListSegmentSubscriptionEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Events") is not None:
        import capo_customer_profiles.types.subscription_events_list

        out["events"] = (
            capo_customer_profiles.types.subscription_events_list.deserialize_json(
                data["Events"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
