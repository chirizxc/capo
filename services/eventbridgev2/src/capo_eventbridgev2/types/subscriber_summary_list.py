"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#SubscriberSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridgev2.types.subscriber_summary

SubscriberSummaryList: TypeAlias = list[
    "capo_eventbridgev2.types.subscriber_summary.SubscriberSummary"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SubscriberSummaryList) -> list:
    import capo_eventbridgev2.types.subscriber_summary

    out: list = []
    for item in value:
        out.append(capo_eventbridgev2.types.subscriber_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SubscriberSummaryList:
    import capo_eventbridgev2.types.subscriber_summary

    out: SubscriberSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_eventbridgev2.types.subscriber_summary.deserialize_cbor(item))
    return out
