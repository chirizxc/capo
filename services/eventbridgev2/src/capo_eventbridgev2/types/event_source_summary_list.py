"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#EventSourceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridgev2.types.event_source_summary

EventSourceSummaryList: TypeAlias = list[
    "capo_eventbridgev2.types.event_source_summary.EventSourceSummary"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventSourceSummaryList) -> list:
    import capo_eventbridgev2.types.event_source_summary

    out: list = []
    for item in value:
        out.append(capo_eventbridgev2.types.event_source_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EventSourceSummaryList:
    import capo_eventbridgev2.types.event_source_summary

    out: EventSourceSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_eventbridgev2.types.event_source_summary.deserialize_cbor(item))
    return out
