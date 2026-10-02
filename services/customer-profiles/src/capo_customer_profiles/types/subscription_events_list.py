"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SubscriptionEventsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.subscription_event_item

SubscriptionEventsList: TypeAlias = list[
    "capo_customer_profiles.types.subscription_event_item.SubscriptionEventItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionEventsList) -> list:
    import capo_customer_profiles.types.subscription_event_item

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.subscription_event_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SubscriptionEventsList:
    import capo_customer_profiles.types.subscription_event_item

    out: SubscriptionEventsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_customer_profiles.types.subscription_event_item.deserialize_json(item)
        )
    return out
