"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#PutRawEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.integer
    import capo_eventbridgev2.types.put_raw_events_result_entry_list


class PutRawEventsResponse(TypedDict, closed=True):
    failed_entry_count: "capo_eventbridgev2.types.integer.Integer"
    """The number of entries in the batch that failed to be published."""
    entries: NotRequired[
        "capo_eventbridgev2.types.put_raw_events_result_entry_list.PutRawEventsResultEntryList"
    ]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutRawEventsResponse) -> dict:
    out: dict = {}
    out["FailedEntryCount"] = value.get("failed_entry_count", 0)
    if "entries" in value:
        import capo_eventbridgev2.types.put_raw_events_result_entry_list

        out["Entries"] = (
            capo_eventbridgev2.types.put_raw_events_result_entry_list.serialize_cbor(
                value["entries"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> PutRawEventsResponse:
    out: PutRawEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("FailedEntryCount") is not None:
        out["failed_entry_count"] = data["FailedEntryCount"]
    else:
        out["failed_entry_count"] = 0
    if data.get("Entries") is not None:
        import capo_eventbridgev2.types.put_raw_events_result_entry_list

        out["entries"] = (
            capo_eventbridgev2.types.put_raw_events_result_entry_list.deserialize_cbor(
                data["Entries"]
            )
        )
    return out
