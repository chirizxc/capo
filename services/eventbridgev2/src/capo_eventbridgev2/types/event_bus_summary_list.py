"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#EventBusSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridgev2.types.event_bus_summary

EventBusSummaryList: TypeAlias = list[
    "capo_eventbridgev2.types.event_bus_summary.EventBusSummary"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventBusSummaryList) -> list:
    import capo_eventbridgev2.types.event_bus_summary

    out: list = []
    for item in value:
        out.append(capo_eventbridgev2.types.event_bus_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EventBusSummaryList:
    import capo_eventbridgev2.types.event_bus_summary

    out: EventBusSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_eventbridgev2.types.event_bus_summary.deserialize_cbor(item))
    return out
