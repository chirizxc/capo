"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#PutRawEventsResultEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridgev2.types.put_raw_events_result_entry

PutRawEventsResultEntryList: TypeAlias = list[
    "capo_eventbridgev2.types.put_raw_events_result_entry.PutRawEventsResultEntry"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutRawEventsResultEntryList) -> list:
    import capo_eventbridgev2.types.put_raw_events_result_entry

    out: list = []
    for item in value:
        out.append(
            capo_eventbridgev2.types.put_raw_events_result_entry.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> PutRawEventsResultEntryList:
    import capo_eventbridgev2.types.put_raw_events_result_entry

    out: PutRawEventsResultEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_eventbridgev2.types.put_raw_events_result_entry.deserialize_cbor(item)
        )
    return out
